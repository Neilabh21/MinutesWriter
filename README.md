# MinutesWriter [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Takes Google Meet Transcript and converts it into minutes. 
This project was done as a part of the Unscripted project under SoC 2021. 

## Supported Platforms

* Windows/Ubuntu/OSX

## Prerequisites

### Common

* Python

* `transformers` library

	`pip install transformers`
	

* Clone the git repo:

	`git clone https://github.com/Neilabh21/MinutesWriter.git`

## Getting the Meet Transcript

* Install the Chrome Extension - [Meet Trancript](https://chrome.google.com/webstore/detail/meet-transcript/jkdogkallbmmdhpdjdpmoejkehfeefnb?hl=en)

* Download the Transcript generated as `*.txt`.

## Run

### On Terminal / Colab
	
* Run `Transcript_Summariser` with the Transcript `*.txt` file. 
	
	`$ python Transcript_Summariser.py Examples/Transcript1.txt`


