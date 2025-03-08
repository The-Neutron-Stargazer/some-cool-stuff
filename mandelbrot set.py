import numpy as np
import matplotlib.pyplot as plt

def complex_matrix(xmin, xmax, ymin, ymax, size):
    re = np.linspace(xmin, xmax, int((xmax - xmin)*size)                                     )
    im = np.linspace(ymin, ymax, int((ymax - ymin))*size)
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j

def mandelbrot(c, num_itr):
    z = 0
    for _ in range(num_itr):
        z = z ** 2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = mandelbrot(c, num_iterations)
    return c[mask]

c = complex_matrix(-2, 0.5, -1.5, 1.5, size=1024)
plt.imshow(mandelbrot(c, num_itr=20), cmap="binary")
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()