# %% 
import numpy as np
import matplotlib.pyplot as plt
# %% 
# parameters
fs = 44000
f0 = 440
k = 1/fs 
L = 1 # length
sec = 1

c = 2 * L * f0 # wave speed
h = c * k 
N = int(np.floor(L/h)) # intervals
h = L/N
_lambda = (c * k) / h

# %%
uNext = np.zeros(N+1)
u = np.zeros(N+1)
uPrev = np.zeros(N+1)
# %%
u[1] = 1
uPrev = np.copy(u)

out = np.zeros(fs * sec)
lengthSound = fs * sec

# %%
for l in range(1, lengthSound):
    for i in range(1, N):
        next = u[i+1]
        prev = u[i-1]

        uNext[i] = 2 * u[i] - uPrev[i] + (_lambda * _lambda) * (next - 2 * u[i] - prev)

    uPrev = np.copy(u)
    u = np.copy(uNext)
    out[l] = u[4]
    
# %%
plt.plot(out)
plt.show()

# %%