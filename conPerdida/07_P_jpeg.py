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

pi=math.pi




import matplotlib.pyplot as plt




        
"""
Matrices de cuantización, estándares y otras
"""

    
Q_Luminance=np.array([
    [16 ,11, 10, 16,  24,  40,  51,  61],
    [12, 12, 14, 19,  26,  58,  60,  55],
    [14, 13, 16, 24,  40,  57,  69,  56],
    [14, 17, 22, 29,  51,  87,  80,  62],
    [18, 22, 37, 56,  68, 109, 103,  77],
    [24, 35, 55, 64,  81, 104, 113,  92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103,  99]])

Q_Chrominance=np.array([
[17, 18, 24, 47, 99, 99, 99, 99],
[18, 21, 26, 66, 99, 99, 99, 99],
[24, 26, 56, 99, 99, 99, 99, 99],
[47, 66, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99]])

def Q_matrix(r=1):
    m=np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            m[i,j]=(1+i+j)*r
    return m

"""
Implementar la DCT (Discrete Cosine Transform) 
y su inversa para bloques NxN

dct_bloque(p,N)
idct_bloque(p,N)

p bloque NxN

"""
def generateC(size):
    global C
    C = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i == 0:
                C[i, j] = 1 / math.sqrt(size)
            else:
                C[i, j] = (math.sqrt(2.0 / size)) * math.cos(((2.0 * j + 1.0) * i * pi) / (2.0 * size))
    return C
def dct_bloque(p):
    global C
    p = p-128
    return np.tensordot(np.tensordot(C, p, axes=([1],[0])),C,axes=([1],[1]))

def idct_bloque(p):
    global C
    return np.tensordot(np.tensordot(C, p, axes=([0], [1])), C, axes=([1], [0])) + 128

"""
Reproducir los bloques base de la transformación para los casos N=4,8
Ver imágenes adjuntas.
"""


"""
Implementar la función jpeg_gris(imagen_gray) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen de grises 'imagen_gray' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error
Sigma=np.sqrt(sum(sum((imagen_gray-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))


En este caso optimizar la DCT 
http://docs.scipy.org/doc/numpy-1.10.1/reference/routines.linalg.html
"""
def dct2 (block):
  return dct(dct(block.T, norm = 'ortho').T, norm = 'ortho')
def idct2 (block):
  return idct(idct(block.T, norm = 'ortho').T, norm = 'ortho')


def jpeg_gris(imagen_gray):
    #dividimos en bloques 8x8
    block_size = 8
    n, m = imagen_gray.shape
    nbloques = int(n / block_size)
    bloques = []
    for iblock in range(nbloques):
        for jblock in range(nbloques):
            bloque = []
            for i in range(block_size):
                fila = iblock * block_size + i
                for j in range(block_size):
                    bloque += [imagen_gray[fila,jblock * block_size + j]]
            bloques += np.reshape(bloque,(block_size,block_size))
    print(bloques)
    return imagen_gray


"""
Implementar la función jpeg_color(imagen_color) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen RGB 'imagen_color' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error para cada una de las componentes RGB
Sigma=np.sqrt(sum(sum((imagen_color-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_color)**2)))


En este caso optimizar la DCT 
http://docs.scipy.org/doc/numpy-1.10.1/reference/routines.linalg.html
"""



def jpeg_color(imagen_color):
    pass

"""
#--------------------------------------------------------------------------
Imagen de GRISES

#--------------------------------------------------------------------------
"""


### .astype es para que lo lea como enteros de 32 bits, si no se
### pone lo lee como entero positivo sin signo de 8 bits uint8 y por ejemplo al 
### restar 128 puede devolver un valor positivo mayor que 128
def showimage(img):
    plt.imshow(img, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.show()
mandril_gray=scipy.ndimage.imread('test_images/mandril_gray.png').astype(np.int32)
generateC(8)
start= time.clock()
mandril_jpeg=jpeg_gris(mandril_gray)
end= time.clock()
showimage(mandril_jpeg)
print("tiempo",(end-start))


"""
#--------------------------------------------------------------------------
Imagen COLOR
#--------------------------------------------------------------------------
"""
## Aplico.astype pero después lo convertiré a 
## uint8 para dibujar y a int64 para calcular el error

mandril_color=scipy.misc.imread('./test_images/mandril_color.png').astype(np.int32)



start= time.clock()
mandril_jpeg=jpeg_color(mandril_color)     
end= time.clock()
print("tiempo",(end-start))
     
       









