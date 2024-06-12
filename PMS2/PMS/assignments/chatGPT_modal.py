# %%
# libraries 
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# %% 
# define the modal synthesis algorithm

def modal_synthesis(dur, fs):
    time = np.linspace(0, dur, int(fs * dur), endpoint=False)
    waveform = np.zeros_like(time)
    
    mode_freq = [120, 200, 800, 1500]
    decay_factors = [0.80, 0.90, 0.60, 0.70]
    

    # R = np.exp(-dur/fs)
    # theta = 2 * 3.1415 * (1/fs)
    
    for i in range(len(mode_freq)):
        mode = np.sin(2 * np.pi * mode_freq[i] * time)
        print(mode)
        mode *= np.exp(-decay_factors[i] * time)
        waveform += mode

    waveform /= np.max(np.abs(waveform))
    return waveform

# %% 
# running the algorithm 

dur = 2
fs = 44100
signal = modal_synthesis(dur, fs)

plt.plot(np.arange(0, dur, 1/fs), signal)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# %%
# play the sound
sd.play(signal, samplerate=fs)
sd.wait()

# %%
