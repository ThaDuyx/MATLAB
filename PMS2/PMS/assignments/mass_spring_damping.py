# %%
# import libraries
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

# %%
# parameter init
m = 2       # [kg]  mass 
fs = 44100  # [Hz]  sample rate
T = 1/fs    # [s]   time step
N = fs      #       number of samples / duration
k = 5000000 # [N/m] spring coefficient
R = 20      #       damping coefficient. Smaller equals longer signal.

# %%
# displacement init

x = np.zeros(N) # signal array
xm1 = 1         # x[n-1]
xm2 = xm1       # x[n-2] 

c1 = m + R*T + k*(T*T)
c2 = 2*m + R*T

# x[i] = (2*m + R*T) / m + R*T + k*(T*T) * xm1 - xm2*m / m + R*T + k*(T*T) update equation

# %%
# run algorithm and normalize
for i in range(N):
    x[i] = c2/c1*xm1 - xm2*m/c1 # mass spring damping equation
    xm2 = xm1   # update x[n-2] sample 
    xm1 = x[i]  # update x[n-1] sample

sig = x
sig /= np.max(np.abs(sig))

# %% 
# plot signal
plt.plot(np.arange(0, 1, T), sig)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# %%
# play sound
sd.play(sig)
sd.wait()

# %%
