# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import scipy as sc
import scipy.ndimage
from scipy import misc
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

def dct_bloque (block):
  return dct(dct(block.T, norm = 'ortho').T, norm = 'ortho')
def idct_bloque (block):
  return idct(idct(block.T, norm = 'ortho').T, norm = 'ortho')

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
'''def dct_bloque(p):
    global C
    p = p-128
    return np.tensordot(np.tensordot(C, p, axes=([1],[0])),C,axes=([1],[1]))

def idct_bloque(p):
    global C
    return np.tensordot(np.tensordot(C, p, axes=([0], [1])), C, axes=([1], [0])) + 128'''


"""
Reproducir los bloques base de la transformación para los casos N=4,8
Ver imágenes adjuntas.
"""
def showMatrices(size):
    img = plt.figure()
    mat = np.zeros((size,size))
    mat = mat.astype(int)
    for i in range(size):
        for j in range(size):
            mat[i,j] = 1
            res = idct_bloque(mat)
            img.add_subplot(size,size, i * size + j + 1).axis('off')
            plt.imshow(sc.misc.toimage(res.reshape((size,size))))

            mat[i,j] = 0
print('calculating matrix N = 4')
generateC(4)
showMatrices(4)
print('calculating matrix N = 8')
generateC(8)
showMatrices(8)


plt.show()


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
global coef_Non_zero
coef_Non_zero = 0

def jpeg_gris(imagen_gray):
    global coef_Non_zero
    #dividimos en bloques 8x8
    block_size = 8
    n, m = imagen_gray.shape
    res = np.zeros((n,m))
    for i in range(0,n,block_size):
        for j in range(0,m,block_size):
            #cojemos bloque
            bloque = imagen_gray[i : i + block_size, j : j + block_size]

            #restamos 128
            bloque -= 128

            #contamos los que no sean zeros, para poder hacer luego la estimacion
            coef_Non_zero = coef_Non_zero + np.count_nonzero(bloque)
            #aplicamos dct y quantizamos
            dct = dct_bloque(bloque)
            cuantizado = np.around(np.divide(dct,Q_Luminance))

            #recuperamos
            idct = idct_bloque(np.multiply(cuantizado, Q_Luminance))
            idct += 128
            res[i: i +block_size,j: j + block_size] = idct

    return res


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
def RGBtoYCbCr(image):
    n, m, components = image.shape
    newImage = np.zeros(image.shape)
    for i in range(n):
        for j in range(m):
            pixel = image[i,j]
            newPixel = np.zeros((3))
            newPixel[0] = pixel[0] * 75/256 + pixel[1] * 150/256 + pixel[2] * 29/256 #Y
            newPixel[1] = pixel[0] * -44/256 + pixel[1] * -87/256 + pixel[2] * 131/256 + 128 #Cb
            newPixel[2] = pixel[0] * 131/256 + pixel[1] * -110/256 + pixel[2] * -21/256 + 128 #Cr
            newImage[i,j] = newPixel
    return newImage

def YCbCrtoRGB(image):
    n, m, components = image.shape
    newImage = np.zeros(image.shape)
    for i in range(n):
        for j in range(m):
            pixel = image[i, j]
            newPixel = np.zeros((3))
            newPixel[0] = pixel[0] + 1.371 * (pixel[2] - 128) # R
            newPixel[1] = pixel[0] - 0.698 * (pixel[2] - 128) - 0.336 * (pixel[1] - 128)# G
            newPixel[2] = pixel[0] + 1.732 * (pixel[1] - 128)# B
            newImage[i, j] = newPixel
    return newImage

mat128 = np.full((8, 8, 3), 128)
coef_Non_zero = 0
def jpeg_color(imagen_color):
    global coef_Non_zero
    block_size = 8
    RGBtoYCbCr(imagen_color)
    n, m, components = imagen_color.shape
    res = np.zeros(imagen_color.shape)
    for i in range(0,n,block_size):
        for j in range(0,m,block_size):
            #cojemos bloque
            bloque = imagen_color[i:i+block_size,j:j+block_size]

            bloque = np.subtract(bloque, mat128)
            #aplicamos la dct a cada una de las componentes
            dct = np.zeros((block_size,block_size,3))
            dct[:, :, 0] = dct_bloque(bloque[:, :, 0])
            dct[:, :, 1] = dct_bloque(bloque[:, :, 1])
            dct[:, :, 2] = dct_bloque(bloque[:, :, 2])

            #cuantizamos cada componente
            cuantizado = np.zeros((block_size, block_size, 3))
            cuantizado[:, :, 0] = np.divide(dct[:, :, 0],Q_Luminance)
            cuantizado[:, :, 1] = np.divide(dct[:, :, 1],Q_Chrominance)
            cuantizado[:, :, 2] = np.divide(dct[:, :, 2],Q_Chrominance)
            cuantizado = np.around(cuantizado)
            #contamos los que no sean 0

            coef_Non_zero = coef_Non_zero + np.count_nonzero(bloque[:, :, 0])
            coef_Non_zero = coef_Non_zero + np.count_nonzero(bloque[:, :, 1])
            coef_Non_zero = coef_Non_zero + np.count_nonzero(bloque[:, :, 2])
            #recuperamos
            idct = np.zeros((block_size, block_size, 3))
            idct[:, :, 0] = idct_bloque(np.multiply(cuantizado[:, :, 0], Q_Luminance))
            idct[:, :, 1] = idct_bloque(np.multiply(cuantizado[:, :, 1], Q_Chrominance))
            idct[:, :, 2] = idct_bloque(np.multiply(cuantizado[:, :, 2], Q_Chrominance))


            idct = np.add(idct, mat128)
            res[i:i + block_size, j:j + block_size] = idct
    return res

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
print('calculating jpeg_gris')

n, m = mandril_gray.shape
mandril_jpeg=jpeg_gris(mandril_gray)
end= time.clock()
print("time",(end-start))
print('estimated error(#coefficients / #non-zero coefficients)',n*m/coef_Non_zero)
print('sigma',np.sqrt(sum(sum((mandril_gray-mandril_jpeg)**2)))/np.sqrt(sum(sum((mandril_gray)**2))))
showimage(mandril_jpeg)


"""
#--------------------------------------------------------------------------
Imagen COLOR
#--------------------------------------------------------------------------
"""
## Aplico.astype pero después lo convertiré a 
## uint8 para dibujar y a int64 para calcular el error

mandril_img=scipy.misc.imread('./test_images/mandril_color.png').astype(np.int32)
print('starting color_jpeg')
start= time.clock()
mandril_YCbCr = RGBtoYCbCr(mandril_img)

mandril_q = jpeg_color(mandril_YCbCr)

mandril_final = YCbCrtoRGB(mandril_q)

mandril_final = np.array(mandril_final, dtype=np.float64) / 255
end= time.clock()
print("tiempo",(end-start))
print('estimated error(#coefficients / #non-zero coefficients)',n*m*3/coef_Non_zero)
sigmaR = np.sqrt(sum(sum((mandril_img[:][:][0] - mandril_final[:][:][0]) ** 2))) / np.sqrt(sum(sum((mandril_img[:][:][0]) ** 2)))
sigmaG = np.sqrt(sum(sum((mandril_img[:][:][1] - mandril_final[:][:][1]) ** 2))) / np.sqrt(sum(sum((mandril_img[:][:][1]) ** 2)))
sigmaB = np.sqrt(sum(sum((mandril_img[:][:][2] - mandril_final[:][:][2]) ** 2))) / np.sqrt(sum(sum((mandril_img[:][:][2]) ** 2)))
print('sigma R', sigmaR)
print('sigma G', sigmaG)
print('sigma B', sigmaB)
plt.imshow(mandril_final)
showimage(mandril_final)
     
       



