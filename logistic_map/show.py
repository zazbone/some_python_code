import matplotlib.pyplot as plt

import numpy as np

from .suite import log_suite_gen


def generation_plot(k=3.85, init_value=0.9, n=100):
    n_axes = np.arange(101)
    u_axes = np.array(list(log_suite_gen(k, init_value, n_max=n)))
    plt.plot(n_axes, u_axes)
    plt.show()
