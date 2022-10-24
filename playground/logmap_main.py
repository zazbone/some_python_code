# Logistic map is my main chaos physics case of studies
# I will do different computation on it as exercise


from libs.logistic_map.suite import log_suite
from libs.logistic_map import show


def test_suite():
    k=3.45
    init_value=0.9
    n_max=100
    print(
        f"Logistical suite value at gen: {n_max} for growth rate: {k} and initial value: {init_value} =>",
        log_suite(k, init_value, n_max)
    )
    show.generation_plot(k, init_value, n_max)


def test_lyap():
    show.lyap_funcof_k()


test_suite()
test_lyap()
