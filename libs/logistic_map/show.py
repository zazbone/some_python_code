import matplotlib.pyplot as plt

import numpy as np

from .suite import log_suite_gen
from .lyapounov import calc_coef


def generation_plot(k=3.45, init_value=0.9, n=100):
    n_axes = np.arange(101)
    u_axes = np.array(list(log_suite_gen(k, init_value, n_max=n)))
    plt.plot(n_axes, u_axes)
    plt.xlim(0, n + 1)
    plt.ylim(0, 1)
    plt.xlabel("generation")
    plt.ylabel("U_n")
    plt.title("Logistical suite")
    plt.grid(True)
    plt.show()


def lyap_funcof_k(k=(0, 4), init_value=0.9):
    """\
    Show evolution of lyapounov coeficient value function of k.
    Run 100 of iterations for each coeficient.
    Compute 100 intermediate value in range of k\
    """
    r_axes = np.linspace(k[0], k[1], 100)
    lyap_axes = np.array([
        calc_coef(r, init_value, 100) for r in r_axes
    ])
    plt.xlim(k[0], k[1])
    plt.ylim(-4, 1)
    plt.xlabel("growth rate (k)")
    plt.ylabel("Lyapounov coeficient")
    plt.title("lyap(k)")
    plt.grid(True)
    plt.plot(r_axes, lyap_axes)
    plt.show()
