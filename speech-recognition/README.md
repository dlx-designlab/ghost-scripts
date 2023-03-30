# Speech Recognition for Talking with Neurons
Scripts in this folder are audio recording and language detecting / speech recognition scripts for "Talking with Neurons"
This script detects what an user says and send its information to TouchDesigner over OSC.

## Overview of scripts (and others)
### ASRHelper.py
Automatic Speech Recognition Library made by Frederic. This script provides "transcribe_asr" generator. It mainly uses openai-whisper so it doesn't needs internet conections one model loaded.
Transcribe_asr of Kenta's modified version returns detected text, language of speech, filename of recorded file and timestamp.
### ASR_Main.py
Example script of ASRHelper.

### hello_multilingual.py
It is Language detection script using ASRHepler (=openai-whisper). It hears and records user's voice via microphone, detect its language and send OSC message includes what language is spoken and duration, volume and timestamp of recorded voice. 

### requirements.txt
A list of libraries which are used in ASRHelper.py and hello_multilingual.py
You should select a version of *PyTorch* which matches your computer and gpu (cuda, metal...)
You can install all of them using pip and command:
`pip install -r requirements.txt`

### month_asking_japanses.py
It is casual version of ASR script. It detect only Japanese and requires internet access. It asks "What month of the year do you most like?" and records user's answer via microphone, detect the month and send OSC message includes the month, duration, volume and timestamp of recorded voice. 

# Setup
I tested following environment, but you may be able to set up your computer.
* macOS 11.7.3 Big Sur
* MBP 2016 13-inch Four Thunderbolt (Intel Mac)
* Python 3.10.9 over pyenv

* All dependencies are written in "requirements.txt"

# Running
* Install all library in "requirements.txt"
* Run a script like:
`python hello_multilingual.py`

### hello_multilingual.py
This script has a some options like:
`python hello_multilingual.py --model small --oscipaddress 10.216.199.146 --oscport 6912`

When you run this script on laptop or PC which doesn't have GPU, I recommend to run with option
`--model tiny`
If you have good GPU, using medium or large models are good option.
