import numpy as np
from numpy.random import random as rd_array

import pyglet
from pyglet.window import Window
from pyglet.shapes import Circle
from pyglet import clock

from random import randint


SCREEN_SIZE = 700
MASS_RADIUS_RATIO = 50


def rd_color():
    return randint(0, 255), randint(0, 255), randint(0, 255)


def clamp(value, a=0.01, b=0.99):
    return max(a, min(value, b))


class StateOfPhases(np.ndarray):
    """\
    position:
        x -> nb_objects elements
        y -> nb_objects elements
    impulsion:
        px -> nb_objects elements
        py -> nb_objects elements
    param:
        masse -> nb_objects elements
        blank -> nb_objects elements\
    """
    def __new__(cls, nb_objects):
        shape = (3, 2, nb_objects)
        buffer = np.empty(shape)
        buffer[0] = rd_array((2, nb_objects))
        buffer[1] = rd_array((2, nb_objects)) * 0.1
        buffer[2] = rd_array((2, nb_objects)) * 0.1 + 0.05
        return super(StateOfPhases, cls).__new__(
            cls,
            shape=(3, 2, nb_objects),
            buffer=buffer
        )

    def step(self, dt, n=1, check_collision=True):
        for i in range(n):
            self[0] = self[0] + self[1] * dt / self[2, 0]
            if check_collision:
                self.check_collision()

    def check_collision(self):
        # Wall collision
        for i, x in enumerate(self[0, 0]):
            if x < 0 or x > 1:
                self[0, 0, i] = clamp(x)
                self[1, 0, i] = -self[1, 0, i]
        for i, y in enumerate(self[0, 1]):
            if y < 0 or y > 1:
                self[0, 1, i] = clamp(y)
                self[1, 1, i] = -self[1, 1, i]
        # Particles collision


class App(Window):
    def __init__(self, n):
        super(App, self).__init__(height=SCREEN_SIZE, width=SCREEN_SIZE)

        self.state_of_phase = StateOfPhases(n)
        self.objects = list(map(
            lambda x: Circle(
                x=x[0] * SCREEN_SIZE,
                y=x[1] * SCREEN_SIZE,
                radius=x[2] * MASS_RADIUS_RATIO,
                color=rd_color()
            ),
            zip(
                self.state_of_phase[0, 0],
                self.state_of_phase[0, 1],
                self.state_of_phase[2, 0]
            )
        ))

    def on_draw(self):
        self.render()

    def cycle(self, dt):
        self.update_pos(dt)
        self.render()

    def update_pos(self, dt):
        self.state_of_phase.step(dt)
        for i, obj in enumerate(self.objects):
            obj.x = self.state_of_phase[0, 0, i] * SCREEN_SIZE
            obj.y = self.state_of_phase[0, 1, i] * SCREEN_SIZE

    def render(self):
        self.clear()
        for obj in self.objects:
            obj.draw()


if __name__ == "__main__":
    my_app = App(10)
    event_loop = pyglet.app.EventLoop()
    clock.schedule_interval(my_app.cycle, interval=0.01)

    @event_loop.event
    def on_window_close(window):
        event_loop.exit()

    pyglet.app.run()
