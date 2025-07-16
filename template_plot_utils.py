import matplotlib.pyplot as plt
# This has some examples https://matplotlib.org/matplotblog/posts/pyplot-vs-object-oriented-interface/


def Setup_global_latex_plt(usetex: bool = True,
                           font_family: str = 'serif',
                           font_size: int = 14,
                           latex_preamble: str = "",
                           use_rb_preamble: bool = False,):
    r"""
    A wrapper function to perform `plt.rcParams.update` with some default
    settings.
    # -------------------------------------------------------------------------
    (call as: [simple])
    Setup_global_latex_plt()

    (call as: [Latex not installed])
    Setup_global_latex_plt(usetex=False)

    (call as: [All options])
    Setup_global_latex_plt(usetex: bool = True,
                           font_family: str = 'serif',
                           font_size: int = 14,
                           latex_preamble: str = "",
                           use_rb_preamble: bool = False)

    # -------------------------------------------------------------------------

    :param usetex: boolean (true/false) to enable LaTeX / TeX interpreter
    :param font_family: (See [1] - at bottom)
    :param font_size:   (see [1]
    :param latex_preamble: This is a string that is what usually appears
                           before the LaTeX `\begin{document}`.
                           This will let you use `\usepackages{}`, but not
                           probably not all will be compatatible or useful.
    :param use_rb_preamble: This enables a snippet of roman-bialek's personal
                           `latex_preamble`.
    :return: (None)

    For further details see the matplotlib documentation:
    [1] https://matplotlib.org/stable/users/explain/text/usetex.html
    """

    if latex_preamble is None:
        # handle possible assumed user behaviour
        latex_preamble = ""

    if use_rb_preamble:
        # should probably be changed to read an external file with your
        # latex setup. (This was roman-bialek's own setup)
        latex_preamble = r"\usepackage{amsmath, bm}" \
             + r"\newcommand{\mrm}[1]{\mathrm{#1}}" \
             + r"\newcommand{\lrbrac}[1]{\left( #1 \right)}" \
             + r"\newcommand{\lrbracS}[1]{\left[ #1 \right]}" \
             + r"\newcommand{\surfint}[2]{ \int_{\partial{}#1} #2 \; \mrm{d}S}"
    # end if

    plt.rcParams.update({
        "text.usetex": usetex,
        "font.family": font_family,
        "text.latex.preamble": latex_preamble,
        "font.size": font_size,
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
    """
    A wrapper function
    :param nx:
    :param ny:
    :param enforce_list_output:
    :return:
    """
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