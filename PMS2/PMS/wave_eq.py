# %% 
# libraries
import numpy as np
import matplotlib.pyplot as plt

# %% 
# parameters
L = 1.0 # Length of the domain
T = 5.0 # Total time
c = 1.0 # wave speed
Nx = 100 # number of spatial grid points
Nt = 1000 # Number of time steps
dx = L / Nx # Spatial step size
dt = T / Nt # Time step size

# %%
# Init arrays
u = np.zeros((Nt, Nx))
x = np.linspace(0, L, Nx)
t = np.linspace(0, T, Nt)

# %%
# Initial conditions
u[0, :] = np.sin(np.pi * x) # initial displacement
u[1, :] = u[0, :]           # initial velocity (same as initial displacement)

# %%
# Explicit finite difference scheme
for n in range(1, Nt - 1):
    for i in range(1, Nx - 1):
        u[n + 1, i] = 2 * u[n, i] - u[n - 1, i] + (c * dt / dx) ** 2 * (u[n, i + 1] - 2 * u[n, i] + u[n, i - 1])

# a = 2
# b = 3
# result = a ** b  # This raises 2 to the power of 3
# print(result)  # Output will be 8

# %%
# plot
plt.figure(figsize=(8, 6))
plt.imshow(u, extent=[0, L, 0, T], origin='lower', aspect='auto')
plt.colorbar(label='Displacement')
plt.xlabel('Position')
plt.ylabel('Time')
plt.title('Wave Equation Solution')
plt.show()

# %%
# plot 2
time_step_to_plot = 500
plt.plot(x, u[time_step_to_plot, :])
plt.xlabel('Position')
plt.ylabel('Displacement')
plt.title(f'Waveform at Time Step {time_step_to_plot}')
plt.show()
# %%
