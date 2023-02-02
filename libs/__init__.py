""""""
import numpy as np


PI2_4 = 4 * np.pi ** 2
def laplacian(xy):
    """
    Compute laplacian of a 2D numpy array using spectral differentiation
    Y is row index, x column index
    """
    ny, nx = xy.shape
    XY = np.fft.rfft2(xy, xy.shape)
    ik = - PI2_4 * np.fft.fftfreq(nx)