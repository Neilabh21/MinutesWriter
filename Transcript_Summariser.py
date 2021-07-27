# Imports
from transformers import pipeline
import math
import os
import re
import sys
import numpy as np

# For suppressing warnings
import warnings
warnings.filterwarnings("ignore")

# Inputs 
title = input("Input title of the meeting: ")
date  = input("Input date of the meeting: ")
you_name = input("Input name of the person recording the meeting: ")

## Setting to use the 0th GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

## Setting to use the bart-large-cnn model for summarization
summarizer = pipeline("summarization")

# Data File Name
file_name = sys.argv[1]

from pathlib import Path
text = Path(file_name).read_text()

# Pre-processing text
text_updated = re.sub(r"([0-1]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9] - ", "", text)
text_updated = re.sub(r"\n\n[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*:\n", "\n ", text_updated)

# Define splitter function for Summarizer
def splitter(n, s):
  pieces = s.split()
  return [" ".join(pieces[i:i+n]) for i in range(0, len(pieces), n)]

# Running Summarizer
summary_text_arr = []
chunk_size = 750
for idx, chunk in enumerate(splitter(chunk_size, text_updated)):
  summary_text_arr.append(summarizer(chunk, max_length=40, min_length=10, do_sample=False)[0]['summary_text'])
  print('%d/%d' % (idx + 1, len(splitter(chunk_size, text_updated))))

# Finding Names
names = re.findall(r"- [a-zA-Z ]*:\n", text)
name_arr = []
for elem in np.unique(np.array(names)):
   name_temp = elem[2:-2]
   if name_temp == "You":
     name_temp = you_name
   name_arr.append(name_temp)
name_arr

# Writing to File
print("Minutes of the Meeting")
print("\nTitle: ", title)
print("Date: ", date)
print("Members Present: ", ', '.join(name_arr))
print("\nMinutes:\n - " + "\n - ".join(summary_text_arr))
print("\n=== End of Meeting ===")
with open("{0}_Summary.{1}".format(*file_name.rsplit('.', 1)), "w") as text_file:
  text_file.write("Minutes of the Meeting")
  text_file.write("\n\nTitle: "+ str(title))
  text_file.write("\nDate: "+ str(date))
  text_file.write("\nMembers Present: " + ', '.join(name_arr))
  text_file.write("\n\nMinutes:\n - " + "\n - ".join(summary_text_arr))
  text_file.write("\n\n=== End of Meeting ===")