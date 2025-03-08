import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anime

x, y = 0,0
x_coordinate = [x]
y_coordinate = [y]
N = 100000 # number of iterations

for i in range(N): # for the probabilistic equation
    r = np.random.uniform(0, 1) # r is any random number between 0 & 1
    if 0<=r<0.01 :
        x, y = 0, 0.16 * y

    elif 0.01<=r<0.86 :
        x, y = 0.85 * x + 0.04 * y, -0.04 * x + 0.85 * y + 1.6

    elif 0.86<=r<0.93 :
        x, y = 0.2 * x - 0.26 * y, 0.23 * x + 0.22 * y + 1.6

    elif 0.93<=r<1.00 :
        x, y = -0.15 * x + 0.28 * y, 0.26 * x + 0.24 * y + 0.44

    x_coordinate.append(x) # adds up all x values
    y_coordinate.append(y) # adds up all y values

colors = np.linspace(0, 1, N+1) # for the gradients, N+1 because it will show an error otherwise
fig, axis = plt.subplots(figsize=(8, 10), facecolor="black")
axis.set_aspect("equal")
axis.axis("off")
magic = axis.scatter(x_coordinate, y_coordinate, c=colors, cmap="hsv", marker=".", s=0.2) # plotting the found values
# try cmap gradients 'viridis' (green shades), 'plasma', 'inferno'(red shades), 'magma' (also red), 'cividis'
def animate_func(frame):
    magic.set_array((colors + frame / 50) % 1) # function to animate, modulus of 1 to make the animation smoother
    return magic,

ani = anime.FuncAnimation(fig, animate_func, frames=200, interval=5, blit=False)
# you can play around the frame rate, intervals, or write a different function to animate
plt.show()