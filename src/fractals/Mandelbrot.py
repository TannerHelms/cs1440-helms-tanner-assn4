"""
Given a coordinate in the complex plane, return the
    iteration count of the Mandelbrot function for that point
"""

from utils import Gradient


def colorOfThePixel(c):
    """Return the color of the current pixel within the Mandelbrot set"""

    z = complex(0, 0)  # z0

    for i in range(len(Gradient.gradient)):
        z = z * z + c  # Get z1, z2, ...
        if abs(z) > 2:
            return Gradient.gradient[i]  # The sequence is unbounded
    return Gradient.gradient[len(Gradient.gradient) - 1]  # Indicate a bounded sequence
