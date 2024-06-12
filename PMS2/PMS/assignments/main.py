# %%
# Import needed libraries
import numpy as np
import sounddevice as sd

# %%
# Define the karplus-strong algorithm using delay lines with the extension of dispertion
def karplus_strong_extension(freq, dur, fs = 44100):
    N = int(fs / freq)
    buffer = np.random.uniform(-1, 1, N)
    decay_factor = 0.98
    position = 0
    samples = []

    for _ in range (int(dur * fs)):
        current_sample = 0.5 * (buffer[position] + buffer[(position + 1) % N])
        buffer[position] = decay_factor * current_sample
        position = (position + 1) % N
        samples.append(current_sample)

    
    return np.array(samples)

# %%
# Define the simple karplus-strong algorithm

def karplus_strong_simple(freq, dur, fs = 44100):
    N = int(fs / freq)
    buffer = np.random.uniform(-1, 1, N)
    current_sample = 0
    previous_value = 0
    

    for _ in range (int(dur * fs)):
        
        return np.array(samples)
    
# %%
# Implement usage of the algorithm
freq = 440
dur = 3
data = karplus_strong_extension(freq, dur)

sd.play(data)
sd.wait()
# %%
