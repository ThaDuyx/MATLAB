# %%
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal.windows import hann
from scipy.io.wavfile import write

# %%
fs = 44100                      # sample rate
f0 = 440                        # fundamental frequency
k = 1 / fs                      # step size
L = 5                           # length

kappa = 1                       # stiffness term

# Marimba params
L = 0.473                       # length
rho = 7850                      # material density (rosewood): 7850 or 800
E = 2.45387e13                  # Young's modulus
I = 4.91e-14                    # moment of inertia
A = 7.85e-07                    # cross-sectional area

sigma0 = 10                    # first damping term: 0.2 or 5
sigma1 = 25                 # second damping term: 0.0697 or 25

kappa = np.sqrt((E*I) / (rho*A))

c = 2 * L * f0                  # wave speed
h = np.sqrt(2 * kappa * k)      # h is something related to step size as well
N = int(np.floor(L / h))        # the actual time step that we use

h = L / N                       # recalculation of h
l = c * k / h                   # lambda

# time vectors
uNext = np.zeros(N+1)           # u^n+1
u = np.zeros(N+1)               # u
uPrev = np.zeros(N+1)           # u^n-1

# initializing the excitation of the system
u[2:9] = hann(7)
uPrev = u.copy()

# setting the run time of the system
seconds = 1
lengthSound = int(fs * seconds)

out = np.zeros(lengthSound)
outIx = int((N+1) / 3)

# %%
for j in range(lengthSound):
    for i in range(2, N-1):
        # uNext[i] = (2 * u[i] - uPrev[i] - ((kappa**2 * k**2) / h**4) * (u[i+2] - 4 * u[i+1] + 6 * u[i] - 4 * u[i-1] + u[i-2]) + sigma0 * k * uPrev[i]) / (1 + sigma1 * k)
        uNext[i] = 2 * u[i] - uPrev[i] - (E * I * k**2) / (rho * A * h**4) * (u[i+2] - 4 * u[i+1] + 6 * u[i] - 4 * u[i-1] + u[i-2]) - (2 * sigma0 / k) * (u[i] - uPrev[i]) + (2 * sigma1 / (k * h**2)) * (u[i+1] - 2 * u[i] + u[i-1] - uPrev[i+1] + 2 * uPrev[i] - uPrev[i-1])
    
    out[j] = uNext[outIx]

    uPrev = u.copy()
    u = uNext.copy()

plt.plot(out)
plt.show()
# %%
write("out.wav", fs, out.astype(np.float32))

# %%
