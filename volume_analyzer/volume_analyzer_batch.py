from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import argparse
import os
import csv


def analyse_audio(file_path):
    # Load the audio file
    audio = AudioSegment.from_file(file_path, format="mp3")

    print(f"Channels Detected: {audio.channels}")
    bursts = [0] * audio.channels

    # Analysis of the audio file - each channel
    for channel in range(audio.channels):
        print(f"Channel {channel + 1}:")
        channel_audio = audio.split_to_mono()[channel]

        # Detect non-silent parts of the audio
        nonsilent_regions = detect_nonsilent(channel_audio, min_silence_len=300, silence_thresh=-20)

        # Calculate the average volume level in dB
        if len(nonsilent_regions) > 0:
            total_volume = sum([channel_audio[start:end].dBFS for start, end in nonsilent_regions])
            average_volume = total_volume / len(nonsilent_regions)
            print(f"Total Non-silent regions: {len(nonsilent_regions)} > {nonsilent_regions} Average Volume Level: {average_volume:.2f} dB")
            bursts[channel] = len(nonsilent_regions)
        else:
            bursts[channel] = 0
            print("No bursts audio detected")

    return bursts

if __name__ == "__main__":
    
    # file_path = "data/Neurons.58_cropped.mp3"

    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument("path", help="Folder path with audio file to be analyzed")
    args = parser.parse_args()
    folder_path = args.path

    # List all files in the folder
    file_list = os.listdir(folder_path)
    
    # Specify the path of a CSV file to store the transcriptions
    csv_file_path = f'{os.path.basename(os.path.dirname(args.path))}_data.csv'

    # Create a CSV file to store the transcriptions
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        csv_row_data = ["File", "Ch1", "Ch2", "Total"]
        writer.writerow(csv_row_data)

        # Loop through the files and read their contents
        for file_name in file_list:
            if os.path.isfile(os.path.join(folder_path, file_name)):  # Check if it's a file (not a directory)
                base_name, extension = os.path.splitext(file_name)
                if extension == '.mp3':
                    # transcribe the file 
                    print(f"Analysing {file_name}...")
                    audio_data = analyse_audio(f"{args.path}{file_name}") 
                    
                    # Write the results to the CSV file
                    csv_row_data = [file_name, audio_data[0], audio_data[1], audio_data[0] + audio_data[1]]
                    writer.writerow(csv_row_data)

    print(f'Reults stored in: "{csv_file_path}"')
