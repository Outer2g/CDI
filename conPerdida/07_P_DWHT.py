# -*- coding: utf-8 -*-


########################################################

import numpy as np
import matplotlib.pyplot as plt

"""
Implementar la DWHT Discrete Walsh-Hadamard Transform y su inversa
para bloques NxN 

dwht_bloque(p,HWH,N) 
idwht_bloque(p,HWH,N) 

p bloque NxN
HWH matriz de la transformación
"""
H8 = np.matrix('1  1  1  1  1  1  1  1;'
               '1 -1  1 -1  1 -1  1 -1;'
               '1  1 -1 -1  1  1 -1 -1;'
               '1 -1 -1  1  1 -1 -1  1;'
               '1  1  1  1 -1 -1 -1 -1;'
               '1 -1  1 -1 -1  1 -1  1;'
               '1  1 -1 -1 -1 -1  1  1;'
               '1 -1 -1  1 -1  1  1 -1')

HWH8 = np.matrix('1  1  1  1  1  1  1  1;'
                 '1  1  1  1 -1 -1 -1 -1;'
                 '1  1 -1 -1 -1 -1  1  1;'
                 '1  1 -1 -1  1  1 -1 -1;'
                 '1 -1 -1  1  1 -1 -1  1;'
                 '1 -1 -1  1 -1  1  1 -1;'
                 '1 -1  1 -1 -1  1 -1  1;'
                 '1 -1  1 -1  1 -1  1 -1')

HWH8 = HWH8 * 1 / (8 ** (1 / 2))

HWH4 = np.matrix('1  1  1  1;'
                 '1  1 -1 -1;'
                 '1 -1 -1  1;'
                 '1 -1  1 -1')

HWH4 = HWH4 * 1 / (4 ** (1 / 2))


# HWH8 = HWH8* 1/(8**(1/2))


def dwht_bloque(p, HWH=HWH8, n_bloque=8):
    return np.tensordot(np.tensordot(HWH, p, axes=([1], [0])), HWH, axes=([1], [0]))


def idwht_bloque(p, HWH=HWH8, n_bloque=8):
    return np.tensordot(np.tensordot(HWH, p, axes=([1], [0])), HWH, axes=([1], [0]))


"""
Reproducir los bloques base de la transformación para los casos N=4,8 (Ver imágenes adjuntas)
"""

N = 4


def crearBloque(x=0, y=0, dimension=8):
    shape = (dimension, dimension)
    m = np.zeros(shape)
    m[x][y] = 1;
    return m


for i in range(N * N):
    x = int(i / 4)
    y = i % 4

    m = crearBloque(x, y, N)

    if (N == 4):
        img = dwht_bloque(m, HWH4, n_bloque=N)
    elif (N == 8):
        img = dwht_bloque(m, HWH8, n_bloque=N)

    print(img)
    print('#####################')