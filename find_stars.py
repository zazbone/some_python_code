"""
Hugly code used to get position and radius of stars on a pixel row
Work on denoised ztf dataset's image'
"""


import numpy as np


def in_row(img, row, rmin, sens):
    """
    Algorithme entrypoint
    """
    colmin = None
    colmax = None
    for col, pixel in enumerate(img[row]):
        if pixel >= sens and colmin is None:
            colmin = col
        if pixel < sens and colmin is not None:
            colmax = col
            ccol = (colmax + colmin) // 2
            rcol = (colmax - colmin) // 2
            
            crow, rrow = find_wight(img, row, ccol, sens)
            r = np.sqrt(rrow ** 2 + rcol ** 2)
            if r >= rmin:
                yield crow, ccol, r  # Why a generator ? Better asking why not
            colmin = None
            colmax = None
            

def find_wight(img, row, ccol, sens):
    ymax = img.shape[0]
    crow = row
    row_max = row
    while row < ymax:
        crow += 1
        if img[crow, ccol] < sens:
            row_max = crow
            break
    
    crow = row
    row_min = row
    while 0 < crow:
        crow -= 1
        if img[crow, ccol] < sens:
            row_min = crow
            break
    cx = (row_max + row_min) // 2
    rx = (row_max - row_min) // 2
    return  cx, rx
