import numpy as np
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self):
        self.time = 0  # Paramètres du système
        self.angle = np.pi / 3.5
        self.angular_speed = 0
        self.angular_acc = 0
        self.k = 0.02
        self.l = 0.4
        self.omega = np.pi * 3

    def L(self):  # Renvoie la longueur L(t)
        return self.l + self.k * np.cos(self.omega * self.time)

    def L_prim(self): # Renvoie la dérivée de L(t)
        return -self.omega * self.k * np.sin(self.omega * self.time)

    def calc_acc(self):  # Modifie l'accélération
        self.angular_acc = -((2*self.L_prim() * self.angular_speed)/self.L()\
         + (g * np.sin(self.angle)) / self.L())

    def __iter__(self):  # Définition du générateur de l'itérable
        return self

    def __next__(self):
        """
        Calcule et renvoie l'angle à chaque instant t de 0 a T
            sous forme d'itérable.
        Renvoie le temps et l'angle.
        """
        if self.time <= T:
            self.calc_acc()
            self.angular_speed += self.angular_acc * dt
            self.angle += self.angular_speed * dt
            self.time += dt
            return self.time, self.angle
        else:
            raise StopIteration


def main():
    pendulum = Pendulum()
    time = []
    teta = []
    for i in iter(pendulum):
        time.append(i[0])
        teta.append(i[1])
    plt.plot(time, teta)
    plt.xlabel("Temps (s)")
    plt.ylabel("Angle Θ (rad)")
    plt.show()


if __name__ == "__main__":
    dt = 0.001
    T = 30  # constantes globales
    g = 9.81
    main()
