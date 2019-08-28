import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(h, w, max_iterations=20):
    y, x = np.ogrid[-1.4:1.4:h * 1j, -2:0.8:w * 1j]
    c = x + y * 1j
    z = c

    divtime = max_iterations + np.zeros(z.shape, dtype=int)
    for i in range(max_iterations):
        z = z ** 2 + c
    diverge = z * np.conj(z) > 2 ** 2  # who is diverging
    div_now = diverge & (divtime == max_iterations)  # who is diverging now
    divtime[div_now] = i  # note when
    z[diverge] = 2  # avoid diverging too much
    return divtime


plt.imshow(mandelbrot(400, 400))
plt.show()
