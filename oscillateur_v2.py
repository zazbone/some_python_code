import numpy as np
import matplotlib.pyplot as plt


class Pendulum:
    def __init__(self):
        self.time = 0
        self.angle = np.pi / 3
        self.radius = 0.1
        self.angular_acc = 0
        self.angular_speed = 0

    def calc_acc(self):
        if self.angle > 0:
            self.angular_acc = (-g * np.sin(self.angle)) / self.radius
        else:
            self.angular_acc = (g * np.sin(self.angle)) / self.radius

    def __iter__(self):
        return self

    def __next__(self):
        if self.time <= T:
            self.calc_acc()
            self.angular_speed += self.angular_acc * dt
            self.angular_speed *= 1 - 0.05 * dt
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
        x_coor.append(pendulum.radius * np.sin(i[0]))
        y_coor.append(-pendulum.radius * np.cos(i[0]))
    plt.plot(angle, speed)
    #plt.plot(time_axes, angle)
    #plt.plot(time_axes, speed)
    #plt.plot(time_axes, acc)
    #plt.plot(time_axes, x_coor)
    #plt.plot(time_axes, y_coor)
    #plt.plot(x_coor, y_coor)
    plt.show()


if __name__ == "__main__":
    dt = 0.001
    T = 100
    g = 9.81 * dt * dt
    main()
