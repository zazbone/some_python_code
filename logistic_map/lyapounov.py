from math import log

from .suite import log_suite_gen, logistic_deriv


def calc_coef(k=3.45, init_value=0.9, n=100):
    """\
    Return the Lyapounov coeficient for a given k coeficient and an init_value.
    n corespond to the numbre of generation, influance the precision
    """
    somme = 0
    for u in log_suite_gen(k, init_value, n_max=n):
        somme += _sum_term(k, u, logistic_deriv, n)
    return somme


def _sum_term(k, value, deriv_func, n):
    """\
    Intermediate calculation function
    """
    dx = deriv_func(k, value)
    abs_log = log(abs(dx))
    return abs_log / n
