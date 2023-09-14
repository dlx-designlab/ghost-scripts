from pydub import AudioSegment
from pydub.silence import detect_nonsilent

file_path = "data/Neurons.55_cropped.mp3"

# Load the audio file
audio = AudioSegment.from_file(file_path, format="mp3")

print(f"Analyzing {file_path}... Channels Detected: {audio.channels}")

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
    else:
        print("No bursts audio detected")
