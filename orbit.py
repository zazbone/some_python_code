import turtle
from utils import my_lib
from random import randrange, randint


def main():
    controle = 0
    sample = []
    for i in range(BALL_NUMBER):
        ball = my_lib.creat_ball()
        ball.goto(randrange(-200, 200), randrange(-200, 200))
        ball.dx = randrange(-1, 1)
        ball.dy = randrange(-1, 1)
        ball.dy *= INITIAL_SPEED
        ball.dy *= INITIAL_SPEED
        ball.color("#{:06x}".format(randint(0, 0xFFFFFF)))
        ball.pendown()
        ball.max_speed = 0
        sample.append(ball)
    while True:
        for ball in sample:
            ball.xacc = 0
            ball.yacc = 0
        for i in range(len(sample)):
            for j in reversed(range(i + 1, len(sample))):
                xcor1 = sample[i].xcor()
                ycor1 = sample[i].ycor()
                xcor2 = sample[j].xcor()
                ycor2 = sample[j].ycor()
                gx, gy = my_lib.calc_acc([xcor1, ycor1], [xcor2, ycor2])
                sample[i].xacc += gx
                sample[i].yacc += gy
                sample[j].xacc -= gx
                sample[j].yacc -= gy
            sample[i].xacc += (my_lib.friction(sample[i].dx, FRICTION_INTENSITY))
            sample[i].yacc += (my_lib.friction(sample[i].dy, FRICTION_INTENSITY))
        for ball in sample:
            if controle < BALL_NUMBER:
                print(ball.xacc)
                controle += 1
            #my_lib.changer_couleur(ball)
            my_lib.apply_mvt(ball, ball.xacc, ball.yacc)
            my_lib.hit_border(ball, [screen.window_height(), screen.window_width()])


if __name__ == "__main__":
    FRICTION_INTENSITY = -.0004  # friction coeficient for code simplification, ideal = -.0004
    GRAVITY_INTENSITY = 5  # ideal 5
    BALL_NUMBER = 3  # ideal 3
    INITIAL_SPEED = 0.1  # ideal .1
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Que c'est moche")
    main()
