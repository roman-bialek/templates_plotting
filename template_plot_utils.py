import matplotlib.pyplot as plt
# This has some examples https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/


def Setup_global_latex_plt():
    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "serif",
        "text.latex.preamble": r"\usepackage{amsmath, bm}"
                             + r"\newcommand{\mrm}[1]{\mathrm{#1}}"
                             + r"\newcommand{\lrbrac}[1]{\left( #1 \right)}"
                             + r"\newcommand{\lrbracS}[1]{\left[ #1 \right]}"
                             + r"\newcommand{\surfint}[2]{ \int_{\partial{}#1} #2 \; \mrm{d}S}",
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

    for ax in axs.reshape(-1):
        setup_axis__(ax)

    if enforce_list_output:
        axs = axs.reshape(-1) # force flatten

    return fig, axs

def setup_axis__(ax):
    ax.grid(visible=True, which="major", linestyle="-")
    ax.grid(visible=True, which="minor", linestyle=":")

    # Enable dash-marks on both the specified sides
    # default is {left, bottom} := true; rest = false
    ax.tick_params(which = 'both',
                   bottom=True,
                   top=True,
                   left=True,
                   right=True)

    # gotchya: https://stackoverflow.com/questions/19940518/cannot-get-minor-grid-lines-to-appear-in-matplotlib-figure
    ax.minorticks_on()


    return