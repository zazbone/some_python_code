def log_suite(k=3.45, init_value=0.9, n_max=100):
    """\
    Compute the logistical suite: u_n+1 = k * u_n(1 - u_n)
    And return u_n value for n = n_max
    k: Growth factor for the logistical suite
    """
    u = init_value
    for _ in range(1, n_max + 1):
        u = k * u * (1 - u)
    return u


def log_suite_gen(k=3.45, init_value=0.9, n_max=None):
    """\
    Generator version of the logistical suite
    n_max: If set as default value function will not raise StopIteration
    u_[0-n_max]
    """
    n = 0
    u = 0
    u_next = init_value

    # Run will n < n_max or if n_max set as default
    while (not n_max) or n <= n_max:
        n += 1
        u = u_next
        u_next = k * u_next * (1 - u_next)
        yield u


def logistic_deriv(k, x):
    """\
    Derivation function of the logistical map function.
    Will return logistical map variation for a given x value and k factor
    """
    return k - 2 * k * x
