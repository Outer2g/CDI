# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import scipy
import scipy.ndimage
import math
import copy
import matplotlib.pyplot as plt

import time

from scipy.fftpack import dct, idct

pi = math.pi

import matplotlib.pyplot as plt

def dct_bloque(p):
    global C
    p = p - 128
    return np.tensordot(np.tensordot(C, p, axes=([1], [0])), C, axes=([1], [1]))

m1 = [[2,2,3],[-2,2,0],[-6,-6,8]]
print(np.tensordot(m1,np.transpose(m1),axes=([1],[0])))
print(' ')
m2 =[[2,2,3],[4,4,6],[-6 ,-6,8]]
print(np.tensordot(m2,np.transpose(m2),axes=([1],[0])))
print(' ')
x = 2*math.sqrt(17) / 17
y = 3*math.sqrt(17)/17
z= math.sqrt(2)/2
a = math.sqrt(2) * 3 / 4
q = -3*math.sqrt(34)/34
w = 2*math.sqrt(34)/17
m3 = [[x,x,y],[z,z,a],[q,q,w]]
print(np.tensordot(m3,np.transpose(m3),axes=([1],[0])))
print(' ')
x = 2*math.sqrt(17) / 17
y = 3*math.sqrt(17)/17
z= math.sqrt(2)/2
a = math.sqrt(2) * 3 / 4
q = -3*math.sqrt(34)/34
w = 2*math.sqrt(34)/17
m4 = [[x,x,y],[-z,z,0],[q,q,w]]
print(np.tensordot(m4,np.transpose(m4),axes=([1],[0])))
print(' ')