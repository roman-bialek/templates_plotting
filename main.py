# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
# This has some examples https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/
import numpy as np
from fontTools.ttLib.scaleUpem import visit


def Setup_global_latex_plt():
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "text.latex.preamble": r"\usepackage{amsmath}",
        "font.size": 14,
    })
    return

def Gen_fig(nx = 1, ny = 1, enforce_list_output = True):
    fig, axs = plt.subplots(nx, ny)

    if (nx == 1 and ny == 1):
        setup_axis__(axs)
        if (enforce_list_output):
            axs = [axs]

        return fig, axs

    for ax in axs:
        setup_axis__(ax)
    return fig, axs

def setup_axis__(ax):
    ax.grid(visible=True, which="major")
    ax.grid(visible=True, which="minor")
    return


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def plot_example(ax):
    time = np.linspace(0, 10, 20)

    g = 9.8  # m/s^2

    velocity = g * time
    distance = 0.5 * g * np.power(time, 2)

    ax.plot(time, distance, label = "Distance $x$ [m]")
    ax.plot(time, velocity, label = r"Velocity $v$ $\left[ \mathrm{m \cdot{} s^{-1}} \right]$")

    ax.set_xlabel("Time $t$ [s]")
    ax.set_ylabel("Variable")

    ax.legend(loc = "best")

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Setup_global_latex_plt()

    f, ax = Gen_fig(nx = 1, ny = 1, enforce_list_output = True)

    plot_example(ax[0])


    plt.show()

    f.savefig("myplot.pdf", format="pdf", bbox_inches="tight")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
