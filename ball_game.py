import pygame
from random import randint
from math import sqrt


class Ball:
    def gravity(self, x, y, dt):
        X = abs(self.x - x)
        Y = abs(self.y - y)
        if X < 1: X = 1
        if Y < 1: Y = 1
        norme = X * X + Y * Y
        cos_alpha = X / norme
        sin_alpha = Y / norme
        gx = (dt / norme) * cos_alpha
        gy = (dt / norme) * sin_alpha
        if not self.x < x: gx *= -1
        if not self.y < y: gy *= -1
        return gx, gy

    def __init__(self, config):
        self.config = config
        self.x_acc = 0
        self.y_acc = 0
        self.x_speed = 0
        self.y_speed = 0
        self.x = randint(-100, 100)
        self.y = randint(-100, 100)
        self.dic_fun = {
            "grav": self.gravity
        }
        self.interaction = self.dic_fun[config]


class Game:
    def __init__(self, ball_number):
        self.ball_list = [Ball("...") for _ in range(ball_number)]
        self.ball_number = ball_number

    def update(self):
        i = self.ball_number + 1
        for ball in self.ball_list:
            x_acc, y_acc = 0, 0
            for j in range(self.ball_number, i, -1):
                i += 1
                x, y = ball.x, ball.y
                x_acc, y_acc += ball.interaction(x, y, dt)


if __name__ == "__main__":
    a = Ball("grav")
    print(a.gravity(2, 2, 1))
