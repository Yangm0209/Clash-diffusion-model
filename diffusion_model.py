import numpy as np
import matplotlib.pyplot as plt

def plot_profile(grid, elevation, color="r", title=None, output=None):
    plt.figure()
    plt.plot(grid, elevation, color)
    plt.xlabel("x")
    plt.ylabel("z")
    
    if title != None:
        plt.title(title)

    if output != None:
        plt.savefig(output)

def calculate_stable_time_step(grid_spacing, diffusivity):
    dt = 0.5 * grid_spacing **2 / diffusivity

    return dt

D = 100  # diffusivity
Lx = 300 # model domain

dx = 0.5 # grid spacing
x = np.arange(start=0, stop=Lx, step=dx)
nx = len(x)

dt = calculate_stable_time_step(dx, D)
nt = 5000

z = np.zeros_like(x)
z_left = 500
z_right = 0
z[ :nx//2] = z_left
z[nx//2: ] = z_right

plot_profile(x, z, "r", "Initial hillslope profile", "Initial_hillslope_profile.png")

for t in range(0, nt):
	z[1:-1] += D * dt / dx ** 2 * (z[:-2] - 2*z[1:-1] + z[2:])

plot_profile(x, z, "b", "Final hillslope profile", "Final_hillslope_profile.png")