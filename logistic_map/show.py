import matplotlib.pyplot as plt

import numpy as np

from logistic_map.suite import log_suite_gen


def generation_plot(k=3.85, init_value=0.9):
    axes_data = np.array(
        list([n, u] for n, u in zip(range(101), log_suite_gen(k, init_value)))
    )
    plt.plot(axes_data[...][0], axes_data[...][1])
    plt.show()
