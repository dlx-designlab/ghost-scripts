#!/usr/bin/env python
# coding: utf-8

import speech_recognition as sr
from datetime import datetime
import wave
import pydub
import numpy as np
import argparse
from pythonosc import udp_client
from pythonosc.osc_message_builder import OscMessageBuilder

from sys import platform
from ASRHelper import transcribe_asr # Frederic's Helper Script

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="tiny", help="Model to use",
                        choices=["tiny", "base", "small", "medium", "large"])
    #parser.add_argument("--non_english", action='store_true',
    #                    help="Don't use the English model.")
    parser.add_argument("--energy_threshold", default=1000,
                        help="Energy level for mic to detect.", type=int)
    parser.add_argument("--record_timeout", default=2,
                        help="How real-time the recording is in seconds.", type=float)
    parser.add_argument("--phrase_timeout", default=3,
                        help="How much empty space between recordings before we "
                             "consider it a new line in the transcription.", type=float)
    parser.add_argument("--default_microphone", default='pulse' if 'linux' in platform else None,
                        help="Default microphone name for SpeechRecognition. "
                             "Run this with 'list' to view available Microphones.", type=str)
                             
    parser.add_argument("--oscipaddress", default='localhost',
                        help="Where will this program send osc signals.", type=str)
                        
    parser.add_argument("--oscport", default='6140',
                        help="What port will this program send osc signals to.", type=int)

    args = parser.parse_args()

    # Initialize the generator with the specified arguments
    transcriber = transcribe_asr(model=args.model,
                                 non_english=True,
                                 energy_threshold=args.energy_threshold,
                                 record_timeout=args.record_timeout,
                                 phrase_timeout=args.phrase_timeout,
                                 default_microphone=args.default_microphone)

    IP = args.oscipaddress
    PORT = args.oscport

    language = None


    while True:
        try:
            # Continuously transcribe speech using the transcriber object
            for line, language, filename, now in transcriber:
                if 'Hello' in line or 'hello' in line:
                    language = 'en'
                print(line)
                print(language)
                # Load the recorded audio data
                sound = pydub.AudioSegment.from_file(filename, format="wav")

                # Split the audio data based on silence, with parameters set to keep only the portions of speech
                chunks = pydub.silence.split_on_silence(sound, min_silence_len=200, silence_thresh=-45, keep_silence=50)

                # Find the longest speech segment
                longest_chunk_duration = 0.
                longest_chunk_id = 0
                for i, chunk in enumerate(chunks):
                    if chunk.duration_seconds > longest_chunk_duration:
                        longest_chunk_duration = chunk.duration_seconds
                        longest_chunk_id = i

                # Export the longest speech segment to a new WAV file
                chunks[longest_chunk_id].export(filename[:-4] + "_splited_" + str(i) + "_lang_" + str(language) + ".wav" , format="wav")

                # Calculate the RMS value of the audio data to get the volume of speech
                data = chunks[longest_chunk_id]
                data = np.array(chunks[longest_chunk_id].get_array_of_samples())
                x = data[::sound.channels]
                rms = np.sqrt(np.mean(np.square(x)))

                # Send various information to the OSC server, including language code, RMS value, duration of speech, and timestamp
                client = udp_client.UDPClient(IP, PORT)

                msg_l = OscMessageBuilder(address='/speech/language')
                msg_l.add_arg(language)
                m_l = msg_l.build()

                msg_r = OscMessageBuilder(address='/speech/rms')
                msg_r.add_arg(rms)
                m_r = msg_r.build()

                msg_d = OscMessageBuilder(address='/speech/duration')
                msg_d.add_arg(longest_chunk_duration)
                m_d = msg_d.build()

                msg_t = OscMessageBuilder(address='/speech/time')
                msg_t.add_arg(str(now))
                m_t = msg_t.build()

                client.send(m_l)
                client.send(m_r)
                client.send(m_d)
                client.send(m_t)

                # Print out the language code, RMS value, duration, and timestamp for debugging purposes
                print("language: " + str(language))
                print("rms: " + str(rms))
                print("duration: " + str(longest_chunk_duration))
                print("time: " + str(now))
                

        # Allow the program to be terminated with a keyboard interrupt
        except KeyboardInterrupt:
            pass
        
    

if __name__ == "__main__":
    main()
