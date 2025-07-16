import numpy as np
import template_plot_utils as tpu

if __name__ == "__main__":
    # (1) This command setups up the formatting for all your matplotlib plots in this file
    tpu.Setup_global_latex_plt(usetex=True)
    # If you encounter a "latex not found" type error, set `usetex=False`

    # (2) Here we define the sub-plot grid size, e.g., 3 by 2
    #     - In this example, we will only use a single axes.
    nx_user = 1
    ny_user = 1
    f, axs = tpu.Gen_fig(nx=nx_user,ny=ny_user, enforce_list_output=True)
    ax = axs[0]

    # (3) Plotting stuff
    x_ = np.linspace(0, np.pi)
    y_ = 2.0 * np.sin(x_)
    ax.plot(x_,
            y_,
            marker = 'o',
            markersize = 5,)
    ax.set_xlabel("$x$")
    ax.set_ylabel(r"Projected happiness $\widehat{y}/\pi$") # random words


    # (4) Visualise or optionally save as a `.pdf`
    f.show()
    # Change `False` to `True` to enable a local save
    if False:
        f.savefig("plot.pdf", format="pdf", bbox_inches="tight")