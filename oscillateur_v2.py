import numpy as np
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self):
        self.time = 0
        self.angle = np.pi / 3
        self.radius = 1
        self.k = 0.1
        self.l
        self.omega = 2*np.pi
        self.omega_carre = self.omega * self.omega
        self.angular_acc = 0
        self.angular_speed = 0
        self.m_g = 0.02 * g

    def L(self):
        return self.l + self.k * np.cos(self.omega * self.time)

    def L_prim(self):
        return self.l - self.omega * self.k * np.sin(self.omega * self.time)

    def L_prim2(self):
        return self.l + self.omega**2 * self.k * np.cos(self.omega * self.time)

    def calc_acc(self):
        acc = -self.omega_carre
        if self.angle > 0:
            self.angular_acc = acc
        else:
            self.angular_acc = -acc

    def __iter__(self):
        return self

    def __next__(self):
        if self.time <= T:
            self.calc_acc()
            self.angular_speed += self.angular_acc * dt
            self.angular_speed *= 1 - 0.00 * dt
            self.angle += self.angular_speed
            self.time += dt
            return self.angle, self.angular_speed, self.angular_acc
        else:
            raise StopIteration


def main():

    pendulum = Pendulum()
    time_axes = np.arange(0, T, dt)
    mouvement = iter(pendulum)
    x_coor = []
    y_coor = []
    angle = []
    speed = []
    acc = []
    for i in mouvement:
        angle.append(i[0])
        speed.append(i[1])
        acc.append(i[2])
        x_coor.append((pendulum.radius + pendulum.L()) * np.sin(i[0]))
        y_coor.append(-(pendulum.radius + pendulum.L()) * np.cos(i[0]))
    #plt.plot(angle, speed)
    #plt.plot(time_axes, angle)
    #plt.plot(time_axes, speed)
    #plt.plot(time_axes, acc)
    #plt.plot(time_axes, x_coor)
    #plt.plot(time_axes, y_coor)
    plt.plot(time_axes, x_coor)
    plt.xlabel("t")
    plt.ylabel("x")
    plt.show()


if __name__ == "__main__":
    dt = 0.001
    T = 100
    g = 9.81 * dt * dt
    main()
