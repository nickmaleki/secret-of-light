import math

import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# https://www.desmos.com/calculator/qfsc3soqxb
# https://www.desmos.com/calculator/c8oj1awmhn
# https://math.stackexchange.com/questions/2781755/semicircle-periodic-wave

# To produce a semicircle that ends at x=1
# wavelength = 2
# diameter = wavelength / 2
# radius = diameter / 2


matplotlib.use("TkAgg")


def my_arange(start, end, step):
    return np.linspace(start, end, num=round((end - start) / step), endpoint=False)


max_wavelength = 10
step_size = .1
grid_max = sum(range(1, max_wavelength + 1))
# TODO: Replace the step function with the intertial line
x = my_arange(0, grid_max, step_size)  # replaced linspace with arange

fig, (ax1, ax2) = plt.subplots(2)
# ax1.set_xlim([0, grid_max])
ax1.set_ylim([-max_wavelength, max_wavelength])

ax2.set_ylim([-grid_max, grid_max])


# TODO: In order to generate atoms this equation must be re-written in 3 dimensions. Currently, this equation is 1 Dimensional.
def walter_wave(radius, times):
    output = []

    for time in times:
        # TODO: Sin needs to be computed on the fly
        if time == 0 or radius == 0 or time < int(2*radius):
            output.append(0)
        else:
            output.append(np.sign(math.sin((math.pi * time) / (2 * radius))) * math.sqrt((radius ** 2) - ((time % (2 * radius) - radius) ** 2)) * ((((radius*2)%2) *2) - 1))

    return output


global total
total = []  # TODO: use functional programming to lower space complexity


def animate(i):
    global total
    if i % 1 == 0.0 and (i / 2) < max_wavelength:  # Add waves only at whole wavelengths
        f = walter_wave(i / 2, x)
        ax1.plot(x, f, 'orange')  # update the data

        total = f if not total else [sum(pair) for pair in zip(total, f)]
        # total = f if not total else map((lambda a,b: a+b), zip(total, f))
        ax2.clear()
        # ax2.set_ylim([-max_wavelength*grid_max, grid_max*max_wavelength])
        # ax2.set_ylim([-grid_max, grid_max])

        ax2.plot([0, grid_max], [0, 0])
        ax2.plot(x, total, 'blue')



ani = animation.FuncAnimation(fig, animate, x, interval=25, repeat=False)

plt.xlim(xmin=0, xmax=grid_max)
mng = plt.get_current_fig_manager()
mng.window.state('zoomed')

plt.show()
