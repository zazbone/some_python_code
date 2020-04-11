import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Lorentz:
    def __init__(self):
        self.x = 0
        self.y = 0.1
        self.z = 0

    def dx(self):
        return sigma * (self.y - self.x)

    def dy(self):
        return rho * self.x - self.y - self.x * self.z

    def dz(self):
        return self.x * self.y - beta * self.z

    def change(self):
        self.x += self.dx() * self.dt
        self.y += self.dy() * self.dt
        self.z += self.dz() * self.dt

    def __iter__(self, end=50, dt=0.0001):
        self.n = 0
        self.max = end
        self.dt = dt
        return self

    def __next__(self):
        if self.n < self.max:
            self.n += 1 * self.dt
            self.change()
            return self.x, self.y, self.z
        else:
            raise StopIteration


if __name__ == "__main__":
    print("hello")
    sigma = 10
    beta = 8/3
    rho = 28
    attracteur = Lorentz()
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    x_axes = []
    y_axes = []
    z_axes = []
    for x, y, z in attracteur:
        x_axes.append(x)
        y_axes.append(y)
        z_axes.append(z)
    ax.plot3D(xs=x_axes, ys=y_axes, zs=z_axes, color="blue")
    plt.show()
    print("goodbye")
