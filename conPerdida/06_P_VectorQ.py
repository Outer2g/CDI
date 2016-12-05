# -*- coding: utf-8 -*-
"""

"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans


def callKmeans(path):
    img = misc.imread(path)
    (n, m) = img.shape
    convertedimg = img.astype(float)
    # bloques
    blocksize = 8
    bloques = np.zeros((int(n * m / (blocksize * blocksize)), blocksize * blocksize))
    print(len(bloques))
    for i in range(0, n, blocksize):
        for j in range(0, m, blocksize):
            bloque = img[i:i + blocksize, j:j + blocksize]
            bloques[int(i * n / (blocksize * blocksize) + j / blocksize), :] = np.reshape(bloque, blocksize * blocksize)

    '''kmeans cojera 512 imagenes 8x8. vq seleccionara para cada bloque 8x8, la que mejor se adapta'''
    code_book, d = kmeans(bloques, 512)
    # print(code_book[0])
    dicc, valores = vq(bloques, code_book)
    nblocksize = int(n / blocksize)
    for i in range(nblocksize * nblocksize):
        bloque = code_book[dicc[i]]
        for j in range(blocksize * blocksize):
            x = int(blocksize * int(i / nblocksize) + j / blocksize)
            y = int(j % blocksize + blocksize * int(i % nblocksize))
            img[x][y] = int(bloque[j])

    plt.imshow(img, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.show()
"""
Usando K-means http://docs.scipy.org/doc/scipy/reference/cluster.vq.html
crear un diccionario cuyas palabras sean bloques 8x8 con 512 entradas 
para la imagen de Lena.

Dibujar el resultado de codificar Lena con dicho diccionario.

Calcular el error, la ratio de compresión y el número de bits por píxel
"""
callKmeans('test_images/lena_gray_512.png')

"""
Hacer lo mismo con la imagen Peppers (escala de grises)
http://www.imageprocessingplace.com/downloads_V3/root_downloads/image_databases/standard_test_images.zip
"""
callKmeans('test_images/peppers_gray.png')

"""
Dibujar el resultado de codificar Peppers con el diccionarios obtenido
con la imagen de Lena.

Calcular el error.
"""
img = misc.imread('test_images/lena_gray_512.png')
(n, m) = img.shape
convertedimg = img.astype(float)
# bloques
blocksize = 8
bloquesLena = np.zeros((int(n * m / (blocksize * blocksize)), blocksize * blocksize))
for i in range(0, n, blocksize):
    for j in range(0, m, blocksize):
        bloque = img[i:i + blocksize, j:j + blocksize]
        bloquesLena[int(i * n / (blocksize * blocksize) + j / blocksize), :] = np.reshape(bloque, blocksize * blocksize)
img = misc.imread('test_images/peppers_gray.png')
(n, m) = img.shape
bloquesPep =np.zeros((int(n * m / (blocksize * blocksize)), blocksize * blocksize))
for i in range(0, n, blocksize):
    for j in range(0, m, blocksize):
        bloque = img[i:i + blocksize, j:j + blocksize]
        bloquesPep[int(i * n / (blocksize * blocksize) + j / blocksize), :] = np.reshape(bloque, blocksize * blocksize)
'''kmeans cojera 512 imagenes 8x8. vq seleccionara para cada bloque 8x8, la que mejor se adapta'''
code_book, d = kmeans(bloquesLena, 512)
# print(code_book[0])
dicc, valores = vq(bloquesPep, code_book)
nblocksize = int(n / blocksize)
for i in range(nblocksize * nblocksize):
    bloque = code_book[dicc[i]]
    for j in range(blocksize * blocksize):
        x = int(blocksize * int(i / nblocksize) + j / blocksize)
        y = int(j % blocksize + blocksize * int(i % nblocksize))
        img[x][y] = int(bloque[j])

plt.imshow(img, cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()