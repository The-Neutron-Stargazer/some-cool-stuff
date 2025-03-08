import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# semi-major axis in AU, eccentricity, orbital period in days
planets = {
    "Mercury": (0.39, 0.206, 88),
    "Venus": (0.72, 0.007, 224.7),
    "Earth": (1.00, 0.017, 365.2),
    "Mars": (1.52, 0.093, 687),
    "Jupiter": (5.20, 0.049, 4331),
    "Saturn": (9.58, 0.056, 10747),
    "Uranus": (19.22, 0.046, 30589),
    "Neptune": (30.05, 0.010, 59800)
}

theta = np.linspace(0, 2 * np.pi, 500)

fig, ax = plt.subplots(figsize=(7, 7))
ax.set_facecolor("black")
ax.set_xlim(-35, 35)
ax.set_ylim(-35, 35)
ax.grid(color="white", linestyle="--", linewidth=0.3)
ax.scatter(0, 0, color="yellow", s=200, label="Sun")

orbits = []

for planet, (dist, ecc, period) in planets.items():
    semi_minor_axis = dist * np.sqrt(1 - ecc ** 2)
    x = dist * np.cos(theta) - dist * ecc
    y = semi_minor_axis * np.sin(theta)

    ax.plot(x, y, linestyle=":", label=planet)
    point, = ax.plot([], [], "o", markersize=5)
    orbits.append((dist, ecc, period, point))

ax.legend()
speed_up = 100
def update(frame):
    for dist, ecc, period, point in orbits:
        angle = speed_up * 2 * np.pi * (frame / period)
        x = dist * np.cos(angle) - dist * ecc
        y = dist * np.sqrt(1 - ecc**2) * np.sin(angle)
        point.set_data([x], [y])
    return [p[3] for p in orbits]

ani = animation.FuncAnimation(fig, update, frames=598, interval=10)
plt.show()