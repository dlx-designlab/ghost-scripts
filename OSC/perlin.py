import noise
import numpy as np
import matplotlib.pyplot as plt
import time
import random

# Parameters
duration = 10  # Duration of the waveform in seconds
sampling_freq = 1000  # Sampling frequency (number of samples per second)
num_samples = int(duration * sampling_freq)  # Total number of samples

# Generate a random seed
seed = random.randint(0, 10000)

# Generate Perlin noise waveform
waveform = np.zeros(num_samples)
for i in range(num_samples):
    t = i / sampling_freq  # Time in seconds
    waveform[i] = noise.pnoise1(t, octaves=4, persistence=0.5, lacunarity=2.0, base=seed)

# Normalize waveform to the range [-1, 1]
waveform /= np.max(np.abs(waveform))

# Plot the waveform
time = np.linspace(0.0, duration, num_samples)
plt.plot(time, waveform)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Perlin Noise Waveform')
plt.show()