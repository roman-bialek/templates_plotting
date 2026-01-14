# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
# This has some examples https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/
import numpy as np
from scipy.integrate import solve_ivp

from template_plot_utils import *


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
                    atol = 1e-5,
                    dense_output = False)

    # t_ls = np.linspace(sol.t[0], sol.t[-1], 100)
    ax.plot(sol.t, sol.y[0,:],
            marker = 'o',
            linestyle = '-',
            label = r"Distance $x$ [m]", # and $\surfint{\Omega}{x^2/2}$",
            mfc='none', # disable marker face color
            )
    # ax.plot(time, velocity, label = r"Velocity $v$ $\left[ \mathrm{m \cdot{} s^{-1}} \right]$")
    ax.plot(sol.t, sol.y[1, :],
            marker='s',
            linestyle='-',
            label=r"Velocity $\dot{x}$ $\lrbracS{ \mrm{m \cdot s^{-1} } }$",
            mfc='none',  # disable marker face color
            )

    ax.set_xlabel("Time $t$ [s]")
    ax.set_ylabel(r"State space value $\lrbrac{x, \, \dot{x}}$")

    ax.legend(loc = "best")

    return

def plot_vanderpol_ode_example_dense_output(ax):
    argdict = {"mu" : 2.5}
    sol = solve_ivp(vanderpol_,
                    t_span = (0, 10),
                    y0 = (1, 0),
                    args = (argdict,),
                    rtol = 1e-9,
                    atol = 1e-9,
                    dense_output = True)

    t_ls = np.linspace(sol.t[0], sol.t[-1], 300)
    y_ls = sol.sol(t_ls)
    ax.plot(t_ls, y_ls[0,:],
            marker = 'none',
            linestyle = '-',
            label = r"Distance $x$ [m]", # and $\surfint{\Omega}{x^2/2}$",
            mfc='none', # disable marker face color
            )
    # ax.plot(time, velocity, label = r"Velocity $v$ $\left[ \mathrm{m \cdot{} s^{-1}} \right]$")
    ax.plot(t_ls, y_ls[1, :],
            marker='none',
            linestyle='-',
            label=r"Velocity $\dot{x}$ $\lrbracS{ \mrm{m \cdot s^{-1} } }$",
            mfc='none',  # disable marker face color
            )

    ax.set_xlabel("Time $t$ [s]")
    ax.set_ylabel(r"State space value $\lrbrac{x, \, \dot{x}}$")

    ax.legend(loc = "best")

    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Setup_global_latex_plt(use_rb_preamble=True)

    nx_user = 3
    f, ax = Gen_fig(nx = nx_user, ny = 1, enforce_list_output = True)

    plot_example(ax[0])

    # plot_dense = True
    # # switch_case_ = {0 : plot_vanderpol_ode_example(ax[1])}
    # if (plot_dense):
    #     plot_vanderpol_ode_example_dense_output(ax[1])
    # else:
    #     plot_vanderpol_ode_example(ax[1])
    # backwards compat. issues:
    plot_mode = 2
    match plot_mode:
        case 0:
            plot_vanderpol_ode_example(ax[1])
        case 1:
            plot_vanderpol_ode_example_dense_output(ax[1])
        case 2:
            plot_vanderpol_ode_example(ax[1])
            plot_vanderpol_ode_example_dense_output(ax[2])

    # test resize of figure
    size_ = f.get_size_inches()
    size_[1] = size_[1] * nx_user * 1.5
    print("Warning: using *1.5 on sizing to enforce space between xlabel and sub-ax title")
    f.set_size_inches(size_)

    f.show()

    ax[1].set_title("Title test")
    f.savefig("myplot.pdf", format="pdf", bbox_inches="tight")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
