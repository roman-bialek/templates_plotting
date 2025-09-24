# Recommended Usage
*matplotlib will be required, `requirements.txt` etc. has not yet been implemented*

This is a matplotlib plotting utility that I use to quickly setup my figures and plot my data. Feel free to modify what you need. Hopefully you find this useful too.

*LaTeX will also be required if you wish to use those fonts and packages.*

## 1. Cloning
In your folder of interest, if no `git` repo is present, please:
- (windows) Right click, `open in git bash` (_you will need git installed_)
- (linux/mac) open the folder in a terminal
then enter `git init`, then enter:
```git
git submodule add https://github.com/roman-bialek/templates_plotting.git
```

This will add this repo as a git submodule.

This implies you can use it within a folder that may already have a `.git` folder present.
### (Windows specific / no git)
_On the main git page, you can click the green "code" button, and download as a `zip` file. To run seamlessly with the example in section 3, unzip this file into a sub-folder called `templates_plotting`._

_Alternatively, enter the `templates_plotting` folder and run `readme_example.py`. Note, you will still need to install dependencies. You can use an IDE with most of these installed, e.g. Sypder._
## 2. Importing the python module
Assuming your current directory is `.` and the submodule name is `templates_plotting`, you can import the module as
```python
import templates_plotting.template_plot_utils as tpu
```
## 3. Basic usage
Below is a code snippet for a basic setup (note, `matplotlib` is required)
```python
import numpy as np
import templates_plotting.template_plot_utils as tpu

if __name__ == "__main__":
    # (1) This command setups up the formatting for all your matplotlib
    #     plots in this file
    tpu.Setup_global_latex_plt()

    # (2) Here we define the sub-plot grid size, e.g., 3 by 2
    #     - In this example, we will only use a single axes.
    nx_user = 1
    ny_user = 1
    f, axs = tpu.Gen_fig(nx=nx_user,ny=ny_user, enforce_list_output=True)
    ax = axs[0]

    # (3) Plotting stuff
    x = np.linspace(0, np.pi)
    y = 2.0 * np.sin(x_)
    ax.plot(x,
            y,
            marker = 'o',
            markersize = 5,)
    ax.set_xlabel("$x$")
    ax.set_ylabel(r"Projected happiness $\widehat{y}/\pi$") # random words


    # (4) Visualise or optionally save as a `.pdf`
    f.show()
    # Change `False` to `True` to enable a local save
    if False:
        f.savefig("plot.pdf", format="pdf", bbox_inches="tight")
```

Further examples are present in the `examples.py` file, although they may be a bit messy.
