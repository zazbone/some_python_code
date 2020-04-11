import numpy as np
import matplotlib.pyplot as plt

probabilitee = 0.5
ecart_type = 0.1
bins = np.arange(0, 1, 0.001)
plt.plot(bins, (1 / (np.sqrt(2 * np.pi * np.power(ecart_type, 2)))) * \
    (np.power(np.e, -(np.power((bins - probabilitee), 2) / (2 * np.power(ecart_type, 2))))), linewidth=2, color='r')
plt.show()
