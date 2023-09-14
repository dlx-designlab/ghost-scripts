# Project Ghost Scripts
Scripts for Project Ghost

* Image-processing
Explore of realtime pre-processing for image detection by neuron cells.

* Speech-recognition
Audio recording and language detecting / speech recognition scripts for "Talking with Neurons"
This script detects what an user says and send its information to TouchDesigner using OSC.

* OSC and UDP Communication Scripts
Scripts for sending and receiving OSC messages between TouchDesigner and Python.

* Voice to Text Scripts
Scripts for converting voice to text using Google Cloud Speech-to-Text API. To analyze the data we collected from users during various events.

* Video processing and analysis scripts
Scripts for analyzing video data. To analyze the data we collected during various events.

* Sound processing and analysis scripts
Scripts for analyzing sound data. To analyze the data we collected during various events.


# Setup
Sctipts are written in python and processing
Details of each script are in each folder.

# Handy Commands
The bellow coomands and scrips can come handy when preparing data for analysis.

## FFMPEG:
Batch extract audio from video files (the first 8 seconds):
`for i in *.mov; do ffmpeg -i "$i" -ss 00:00:0.0 -t 8  "${i%.mov}.mp3"; done`

Batch trim video files (last 10 seconds):
 `for i in *.mov; do ffmpeg -sseof -10 -i "$i" -c copy "${i%.mov}_trimmed.mov"; done`

Batch extract audio from video files:
 `for i in *.mov; do ffmpeg -i "$i" "${i%.mov}.mp3"; done`
