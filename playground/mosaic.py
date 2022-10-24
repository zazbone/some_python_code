import numpy as np
from PIL import Image
from sys import argv


img_data = Image.open('in.jpg')
img_arr = np.array(img_data)
#################

height, width, _ = img_arr.shape
nbblock = int(argv[1])
ratio = int(argv[2])
hstep = height // nbblock
wstep = width // nbblock
deltah = hstep // (ratio * 2)
deltaw = wstep // (ratio * 2)


colonne = []
for h in range(0, height - hstep, hstep):
    line = []
    for w in range(0, width - wstep, wstep):
        line.append(img_arr[(h - deltah):(h + deltah), (w - deltaw):(w + deltaw)])
    colonne.append(np.hstack(line))

img_arr = np.vstack(colonne)
print(img_arr.shape)

###################
img_arr = Image.fromarray(img_arr)
img_arr.save("out.jpg")
