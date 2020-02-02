import numpy as np


def main():
    v_x = 10 * dt
    v_y = 20 * dt
    x_coor = 0
    y_coor = 0
    time = 0
    t_coor = np.arange(0, T, dt)
    while True:
        v_y -= g
        x_coor += v_x
        y_coor += v_y
        if y_coor < 0:
            print(x_coor)
            break


if __name__ == "__main__":
    dt = 0.001
    T = 10
    g = 9.81 * dt * dt
    main()
