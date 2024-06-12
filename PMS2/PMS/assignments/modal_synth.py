# %%
# Modal Synthesis
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# %%
# defining the impact model
def random_excitation(fs):
    impact = 2 * np.random.rand(fs)
    impact = impact - np.mean(impact)
    
    return impact

def sinusoidal_excitation(t):
    impact = np.sin(2 * np.pi * 440 * t)
    
    return impact

# %%
# define impact signal parameters
fs = 44100
t = np.arange(0, 1, 1/fs)

impact = random_excitation(fs)
# impact = sinusoidal_excitation(t)

# %% 
# define modal parameters
f1 = 150; f2 = 200; f3 = 800; f4 = 1000

# bandwith is how large the filterband is expanding
band1 = 5; band2 = 2; band3 = 10; band4 = 80

mode1 = np.zeros_like(t); mode2 = np.zeros_like(t)
mode3 = np.zeros_like(t); mode4 = np.zeros_like(t)

R1 = np.exp(-band1/fs); R2 = np.exp(-band2/fs) 
R3 = np.exp(-band3/fs); R4 = np.exp(-band4/fs)

theta1 = 2 * np.pi * (f1 / fs); theta2 = 2 * np.pi * (f2 / fs)
theta3 = 2 * np.pi * (f3 / fs); theta4 = 2 * np.pi * (f4 / fs)

mode1_n1 = 0; mode2_n1 = 0; mode3_n1 = 0; mode4_n1 = 0
mode1_n2 = 0; mode2_n2 = 0; mode3_n2 = 0; mode4_n2 = 0

# %% 
# run the modal synthesis algorithm
for i in range(len(t)):
    mode1[i] = 2 * R1 * np.cos(theta1) * mode1_n1 - R1 * R1 * mode1_n2 + impact[i]
    mode1_n2 = mode1_n1
    mode1_n1 = mode1[i]

    mode2[i] = 2 * R2 * np.cos(theta2) * mode2_n1 - R2 * R2 * mode2_n2 + impact[i]
    mode2_n2 = mode2_n1
    mode2_n1 = mode2[i]

    mode3[i] = 2 * R3 * np.cos(theta3) * mode3_n1 - R3 * R3 * mode3_n2 + impact[i]
    mode3_n2 = mode3_n1
    mode3_n1 = mode3[i]

    mode4[i] = 2 * R4 * np.cos(theta4) * mode4_n1 - R4 * R4 * mode4_n2 + y[i]
    mode4_n2 = mode4_n1
    mode4_n1 = mode4[i]
    

sig = mode1 + mode2 + mode3 + mode4

sig /= np.max(np.abs(sig))

# %%
# plot final signal
plt.plot(np.arange(0, 1, 1/fs), sig)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# %%
# play the signal
sd.play(sig, fs)
sd.wait()
# %%
# Each block/mode is a resonance that forms a resonator
# Every resonance is like a filter that are enhancing or maintaining some kind of resonance

# You can change the impact model for anything you'd like to change the final sound that is made by the system
# Inverse filtering is like white noise being modified by a bunch of filters controlling the resonance