import math

import matplotlib.pyplot as plt
import numpy as np
from functools import reduce


# https://www.desmos.com/calculator/qfsc3soqxb
# https://www.desmos.com/calculator/c8oj1awmhn
# https://math.stackexchange.com/questions/2781755/semicircle-periodic-wave

# To produce a semicircle that ends at x=1
# wavelength = 2
# diameter = wavelength / 2
# radius = diameter / 2

max_wavelength = 10

# Everything is made of cube and sphere, not square and circle.
# TODO: In order to generate atoms this equation must be re-written in 3 dimensions. Currently, this equation is 1 Dimensional.
def walter_wave(radius, times):
    output = []
    for time in times:
        # TODO: Sin needs to be computed on the fly
        output.append(np.sign(math.sin((math.pi * time) / (2 * radius))) * math.sqrt((radius ** 2) - ((time % (2 * radius) - radius) ** 2)))
    return output


# TODO: Replace the step function with the intertial line
x = np.arange(1, sum(range(1, max_wavelength + 1)), .1)  # replaced linspace with arange

for i in range(1, max_wavelength + 1):
    plt.plot(x, walter_wave(i / 2, x), 'orange')


temporary = []  # TODO: use functional programming to lower space complexity
for i in range(1, max_wavelength + 1):
    temporary.append(walter_wave(i / 2, x))

harmony = sum(map(np.array, temporary))
plt.plot(x, harmony, 'blue')

plt.axhline(y=0, color='black')
plt.show()
