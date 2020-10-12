# Logistic map is my main chaos physics case of studies
# I will do different computation on it as exercise


from logistic_map.suite import log_suite, log_suite_gen
from logistic_map.lyapounov import calc_coef
from logistic_map import show


def test():
    print(log_suite(k=3.45, init_value=0.9, n_max=100))

    for n, u in zip(range(101), log_suite_gen(n_max=100)):
        print(f"Gen {n} u={u}")

    print(calc_coef(n=100000))

    show.generation_plot()


test()
