# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
# This has some examples https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/
import numpy as np
from fontTools.ttLib.scaleUpem import visit
from matplotlib.lines import lineStyles
from scipy.integrate import solve_ivp

def Setup_global_latex_plt():
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "text.latex.preamble": r"\usepackage{amsmath}",
        "font.size": 14,
    })

    # SMALL_SIZE = 8
    # MEDIUM_SIZE = 10
    # BIGGER_SIZE = 12

    # plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
    # plt.rc('axes', titlesize=SMALL_SIZE)  # fontsize of the axes title
    # plt.rc('axes', labelsize=MEDIUM_SIZE)  # fontsize of the x and y labels
    # plt.rc('xtick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    # plt.rc('ytick', labelsize=SMALL_SIZE)  # fontsize of the tick labels
    # plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
    # plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title
    return

def Gen_fig(nx = 2, ny = 1, enforce_list_output = True):
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
    ax.grid(visible=True, which="major", linestyle="-")
    ax.grid(visible=True, which="minor", linestyle=":")
    # gotchya: https://stackoverflow.com/questions/19940518/cannot-get-minor-grid-lines-to-appear-in-matplotlib-figure
    ax.minorticks_on()
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

def vanderpol_(t, u, argdict : dict):
    return [u[1],
            argdict["mu"]*(1 - u[0]*u[0]) * u[1] - u[0] ]

def plot_vanderpol_ode_example(ax):
    argdict = {"mu" : 2.5}
    sol = solve_ivp(vanderpol_,
                    t_span = (0, 10),
                    y0 = (1, 0),
                    args = (argdict,),
                    rtol = 1e-5,
                    atol = 1e-5)

    ax.plot(sol.t, sol.y[0,:],
            marker = 'o',
            linestyle = '-',
            label = "Distance $x$ [m]",
            mfc='none', # disable marker face color
            )
    # ax.plot(time, velocity, label = r"Velocity $v$ $\left[ \mathrm{m \cdot{} s^{-1}} \right]$")

    ax.set_xlabel("Time $t$ [s]")
    ax.set_ylabel("Position $x$ [m]")

    ax.legend(loc = "best")

    return


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Setup_global_latex_plt()

    f, ax = Gen_fig(nx = 2, ny = 1, enforce_list_output = True)

    plot_example(ax[0])
    plot_vanderpol_ode_example(ax[1])

    # test resize of figure
    size_ = f.get_size_inches()
    size_[1] = size_[1] * 2
    f.set_size_inches(size_)

    f.show()


    f.savefig("myplot.pdf", format="pdf", bbox_inches="tight")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
