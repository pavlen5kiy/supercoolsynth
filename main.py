import numpy as np
import sounddevice as sd

# Parameters
frequency = 440  # A4 note
duration = 2.0   # seconds
sample_rate = 44100  # samples per second

# Generate time array
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

# Generate sine wave
sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)

# Play sound
sd.play(sine_wave, samplerate=sample_rate)
sd.wait()  # Wait until the sound has finished playing
