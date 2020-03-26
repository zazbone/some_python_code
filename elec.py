import numpy as np
import matplotlib.pyplot as plt


class Condensateur:
    def __init__(self):
        self.inductance = 2000  # L
        self.capacity = 0.0001  # F
        self.resistance = 0.01  # k-ohm
        self.tension = 10
        self.d_tension = 0
        self.d2_tension = 0
        self.k = 0.1
        self.time = 0

    def generateur(self):
        return 10 * np.cos(10**5 * dt)

    def calc_d2u(self):
        self.d2_tension = -(self.resistance/self.inductance) * self.d_tension
        self.d2_tension -= (1 + self.k * self.generateur()) * self.tension / (self.inductance * self.resistance)

    def __iter__(self):
        return self

    def __next__(self):
        if self.time <= T:
            self.calc_d2u()
            self.d_tension += self.d2_tension * dt
            self.tension += self.d_tension * dt
            self.time += dt
            return self.time, self.tension
        else:
            raise StopIteration



def main():
    condensateur = Condensateur()
    x = []
    y = []
    for i in iter(condensateur):
        x.append(i[0])
        y.append(i[1])
    plt.plot(x, y)
    plt.title("Angle Θ fonction du temps")
    plt.xlabel("Temps (s)")
    plt.ylabel("Angle Θ (rad)")
    plt.show()


if __name__ == "__main__":
    dt = 0.0001
    T = 1
    main()
