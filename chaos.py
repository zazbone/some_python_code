import numpy as np
import matplotlib.pyplot as plt
import PIL


r = 3.7
time = np.arange(0, 30)
result = np.zeros(30, float)
z = 0.1
epsilon = 0.0001  # dépend de la précision de r


def suite(z):
    return r * z * (1 - z)


bifurcation = []
for i in time:
    result[i] = z
    z = suite(z)
    if i > 20:
        bifurcation.append(z)


print(bifurcation)
plt.plot(time, result)
plt.show()
