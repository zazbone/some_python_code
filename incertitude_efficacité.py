import numpy as np
import matplotlib.pyplot as plt

def stand_dev(sample, average):
    return np.sqrt(sum([(x-average)**2 for x in sample])/1000)

def gaussian(x, stand_dev, average):
    """Calcul de ke^u(x)"""
    k = 1 / np.sqrt(2 * np.pi * stand_dev * stand_dev)
    e = np.power(np.e, -np.power((x - average), 2) / (2 * np.power(stand_dev, 2)))
    return k*e

N = 1000  # Nombre de tirages
M = 1000  # Nombre d'experiences
probability = 0.50
sample = np.random.binomial(n=N, p=probability, size=M)
exp_average = sum(sample)/M
exp_stand_dev = stand_dev(sample, exp_average)  # Ecart type
# Affichage: Echantillon, Gaussienne théorique, Gaussienne experience
_, x, _ = plt.hist(sample, 50, density=True)
plt.plot(x, gaussian(x, exp_stand_dev, exp_average), 'r--', linewidth=2)
plt.plot(x, gaussian(x, stand_dev(sample, probability * N), probability * N), "g", linewidth=2)
plt.show()
