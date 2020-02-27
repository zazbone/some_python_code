import numpy as np
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self):
        self.time = 0
        self.angle = np.pi / 3
        self.angular_acc = 0
        self.angular_speed = 0
        self.k = 0.02
        self.l = 0.1
        self.omega = np.pi
        self.omega_carre = self.omega * self.omega
        self.m_g = 0.02 * g

    def L(self):
        return self.l + self.k * np.cos(self.omega * self.time)

    def L_prim(self):
        return -self.omega * self.k * np.sin(self.omega * self.time)

    def calc_acc(self):
        self.angular_acc = -(2 * self.L_prim() / self.L() * self.angular_speed + self.m_g / self.L() * np.sin(self.angle))

    def __iter__(self):
        return self

    def __next__(self):
        if self.time <= T:
            self.calc_acc()
            self.angular_speed += self.angular_acc * dt
            self.angle += self.angular_speed * dt
            self.time += dt
            return self.time, self.angular_acc, self.angular_speed, self.angle, self.L()
        else:
            raise StopIteration


def main():
    pendulum = Pendulum()
    time = []
    teta = []
    for i in iter(pendulum):
        time.append(i[0])
        teta.append(i[3])
    plt.plot(time, teta)
    plt.title("Angle Θ fonction du temps")
    plt.xlabel("Temps (s)")
    plt.ylabel("Angle Θ (rad)")
    plt.show()


if __name__ == "__main__":
    dt = 0.001
    T = 100
    g = 9.81
    main()
