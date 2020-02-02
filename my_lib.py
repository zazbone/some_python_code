import turtle
from math import sqrt, floor
from random import randrange


def creat_ball():
    ball = turtle.Turtle()
    ball.shape("circle")
    ball.color("white")
    ball.penup()
    ball.speed("fastest")
    ball.goto(0, 0)
    ball.dy = 0
    ball.dx = 0
    ball.xacc = []
    ball.yacc = []
    return ball


def hit_border(ball, limit):
    if ball.ycor() < -limit[0] / 2 + 10:
        ball.goto(ball.xcor(), -limit[0] / 2 + 10)
        ball.dy *= -0.95
    elif ball.ycor() > limit[0] / 2 - 10:
        ball.goto(ball.xcor(), limit[0] / 2 - 10)
        ball.dy *= -0.95
    if ball.xcor() > limit[1] / 2 - 10:
        ball.goto(limit[1] / 2 - 10, ball.ycor())
        ball.dx *= -0.95
    elif ball.xcor() < -limit[1] / 2 + 10:
        ball.goto(-limit[1] / 2 + 10, ball.ycor())
        ball.dx *= -0.95


def apply_mvt(ball, accx, accy):
    ball.dx += accx
    ball.dy += accy
    ball.sety(ball.ycor() + ball.dy)
    ball.setx(ball.xcor() + ball.dx)


def calc_acc(coor1, coor2, intensity=200):
    X = coor1[0] - coor2[0]
    if X < 0:
        X *= -1
    elif X < 0.01:
        X = 0.1
    Y = coor1[1] - coor2[1]
    if Y < 0:
        Y *= -1
    elif Y < 0.01:
        Y = 0.1
    hypotenuse = sqrt(X ** 2 + Y ** 2)
    cos_alpha = X / hypotenuse
    sin_alpha = Y / hypotenuse
    gx = intensity / hypotenuse * cos_alpha
    gy = intensity / hypotenuse * sin_alpha
    if not coor1[0] < coor2[0]:
        gx *= -1
    if not coor1[1] < coor2[1]:
        gy *= -1
    return gx, gy


def friction(speed, intensity=-.01):
    return speed * intensity


def changer_couleur(ball):
    if ball.dx + ball.dy > ball.max_speed:
        ball.max_speed = ball.dx + ball.dy
    if ball.dx + ball.dy != 0:
        red_value = 255 - floor(254 * ball.max_speed / (ball.dx + ball.dy))
        if red_value < 0:
            red_value *= -1
        if red_value > 255:
            red_value = 254
        red_value = "{:02x}".format(red_value)
        blue_value = floor(254 * ball.max_speed / (ball.dx + ball.dy))
        if blue_value < 0:
            blue_value *= -1
        if blue_value > 254:
            blue_value = 254
        blue_value = "{:02x}".format(blue_value)
        ball.color("#" + red_value + "00" + blue_value)
