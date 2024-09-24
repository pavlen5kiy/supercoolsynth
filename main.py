import numpy as np
import sounddevice as sd

from midi import *

SAMPLE_RATE = 44100

bpm = 120
length = 1 / 4
duration = 1 / (bpm / 60) * 4 * length


for note in get_notes():

    t = np.linspace(0, duration, int(SAMPLE_RATE * duration), endpoint=False)
    sine_wave = 0.5 * np.sin(2 * np.pi * note * 5 * t)

    sd.play(sine_wave, samplerate=SAMPLE_RATE)
    sd.wait()
