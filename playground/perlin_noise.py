import random as rd
import numpy as np
from PIL import Image
from libs.utils.my_lib import ask_int
from time import perf_counter
from scipy.misc import imresize


class Perlin:
    WIDTH = 1080
    HEIGHT = 720

    def __init__(self, seed=0, width=WIDTH, height=HEIGHT):
        self.seed = seed
        self.width = width
        self.height = height
        self.array_image = np.zeros((self.height, self.width), dtype=np.uint8)

    def noise(self):
        for x in range(self.height):
            shift = self.seed * x
            for y in range(self.width):
                rd.seed(x + shift + shift * y)
                self.array_image[x][y] = rd.randint(-1, 1)

    def interpol(self):
        self.array_image = imresize(self.array_image, interp="cubic")

    def save(self):
        self.array_image *= 255
        image = Image.fromarray(self.array_image)
        image.save("out-noise.png")


if __name__ == '__main__':
    seed = ask_int("Give seed value:")
    perlin = Perlin(seed)
    start = perf_counter()
    perlin.noise()
    print("Toke:", perf_counter() - start)
    perlin.interpol()
    perlin.save()
