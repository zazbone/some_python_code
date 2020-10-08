# Calculation of logistical suite's Lyapounov coeficient.
# Instruction: In excel, calculate Lyapounov coeficient for the logistical suite.
# I will do it with python

import numpy as np
from ask import ask
import matplotlib.pyplot as plt


def logistical_suite(initial_value, k):
    current_gen = 0
    next_gen = initial_value
    while True:
        current_gen = next_gen
        next_gen = current_gen * k * (1 - current_gen)
        yield current_gen


def logistical_suite_deriv(x, k):
    return k - 2 * k * x


def lyapounov(N, x_O, k):
    somme = 0
    for n, x in zip(range(N), logistical_suite(x_0, k)):
        dx = logistical_suite_deriv(x, k)
        abs_log = np.log(abs(dx))
        somme += abs_log
        if n != 0:
            yield somme / n
        else:
            yield 0


if __name__ == '__main__':
    N = ask("Number of iteration:", int) + 1
    x_0 = ask("Initial population ratio:", float)
    k = ask("Growing rate:", float)

    iteration = np.arange(N)
    coef_list = np.array(list(lyapounov(N, x_0, k)))

    print(coef_list[-1])
    plt.plot(iteration, coef_list)
    plt.show()
