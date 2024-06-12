# %% 
# import libraries
# The more steps the better the representation of this 
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

# %%
# setup parameters
m = 2 #kg
fs = 44100 # samplerate
T = 1/fs # time step
N = fs # number of samples
k = 5000000 # N/m

# %%
# setup placeholders
# 0.5 is an arbitrary value, we set this because this is how we add force in the system and a way for the system to find out where to start
x = np.zeros(N)
xm1 = 0.5 #x[n-1]
xm2 = xm1 #x[n-2]


for i in range(N):
    x[i] = (2*m)/(m+k*T*T)*xm1 - xm2 *(m)/(m+k*T*T)
    xm2 = xm1
    xm1 = x[i]

sig = x
sig /= np.max(np.abs(sig))
# %% 
# plotting
plt.plot(np.arange(0, 1, T), sig)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()


# %% 
# play the sound
sd.play(sig, fs)
sd.wait()

# What is funny about this system is without the damping coefficient the system should keep growing
# as a sinusoidal wave 

# But our systems will comprimse this by approximation error.
# and actually give a fine result were the length of the sound is controlled by the samplerate used 
# in the calculation
# %%
