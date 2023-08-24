"""Google Cloud Speech API sample application using the REST API for batch
processing.

Example usage:
    python transcribe.py resources/audio.raw
    python transcribe.py gs://cloud-samples-tests/speech/brooklyn.flac
"""

# This script is using Google Cloud App Engine API with dev@designlab.ac account
# To use it, you need to install the Google Cloud SDK and set up the credentials
# See sample tutorial here: https://cloud.google.com/speech-to-text/docs/sync-recognize#perform_synchronous_speech_recognition_on_a_local_file

import argparse
import os
import csv
from google.cloud import speech

def transcribe_file(speech_file: str) -> speech.RecognizeResponse:
    """Transcribe the given audio file."""
    client = speech.SpeechClient()

    # [START speech_python_migration_sync_request]
    # [START speech_python_migration_config]
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED,
        sample_rate_hertz=44000,
        language_code="en-US",
    )
    # [END speech_python_migration_config]

    # [START speech_python_migration_sync_response]
    response = client.recognize(config=config, audio=audio)

    # [END speech_python_migration_sync_request]
    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(f"Transcript: {result.alternatives[0].transcript}")
    # [END speech_python_migration_sync_response]

    return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("path", help="File path for audio file to be recognized")
    args = parser.parse_args()
    folder_path = args.path

    # List all files in the folder
    file_list = os.listdir(folder_path)
    
    # Specify the path of a CSV file to store the transcriptions
    csv_file_path = f'{os.path.basename(os.path.dirname(args.path))}_transcriptions.csv'

    # Create a CSV file to store the transcriptions
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Loop through the files and read their contents
        for file_name in file_list:
            if os.path.isfile(os.path.join(folder_path, file_name)):  # Check if it's a file (not a directory)
                base_name, extension = os.path.splitext(file_name)
                if extension == '.mp3':
                    # transcribe the file 
                    print(f"Transcribing {file_name}...")
                    transcription = transcribe_file(f"{args.path}{file_name}") 
                    
                    # Write the transcription to the CSV file
                    for result in transcription.results:
                        csv_row_data = [file_name, result.alternatives[0].transcript]
                        writer.writerow(csv_row_data)

    print(f'Transcriptions stored in: "{csv_file_path}"')

    
