# -*- coding: utf-8 -*-

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import math



'''imagen = misc.ascent()#Leo la imagen
(n,m)=imagen.shape # filas y columnas de la imagen
plt.imshow(imagen, cmap=plt.cm.gray) 
plt.xticks([])
plt.yticks([])
plt.show() '''
        
"""
Mostrar la imagen habiendo cuantizado los valores de los píxeles en
2**k niveles, k=1..8

Para cada cuantización dar la ratio de compresión y Sigma

Sigma=np.sqrt(sum(sum((imagenOriginal-imagenCuantizada)**2)))/(n*m)

"""
class Range():
    def __init__(self,k):
        self.levels = 2**k
        self.divisions = [math.ceil(i * 255/self.levels) for i in range(self.levels+1)]
        print(self.divisions)
    def Quantization(self,value):
        pos = 0
        for i in self.divisions:
            if i >= value: break
            pos += 1
        return ((self.divisions[pos] - self.divisions[pos-1]) / 2) + self.divisions[pos-1]
img = misc.imread('test_images/lena_gray_512.png')
(n,m) = img.shape
k = 2
distrib = Range(k)
for i in range(n):
    for j in range(m):
        img[i][j] = int(distrib.Quantization(img[i][j]))

plt.imshow(img,cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
imgor = misc.imread('test_images/lena_gray_512.png')
Sigma=np.sqrt(sum(sum((imgor-img)**2)))/(n*m)
print('Sigma: ',Sigma)
ratio = float(256)/float(2**k)
print('ratio: ',ratio)


"""
Mostrar la imagen cuantizando los valores de los pixeles de cada bloque
n_bloque x n_bloque en 2^k niveles, siendo n_bloque=8 y k=2

Calcular Sigma y la ratio de compresión (para cada bloque 
es necesario guardar 16 bits extra para los valores máximos 
y mínimos del bloque, esto supone 16/n_bloque**2 bits más por pixel).
"""
class RangeBlock():
    def __init__(self,k,minimum,maximum):
        self.levels = 2**k
        self.delta = (maximum - minimum) / self.levels
        self.divisions = [minimum]
        for i in range(1,self.levels+1):
            self.divisions += [self.divisions[i-1] + self.delta]
    def Quantization(self,value):
        pos = 0
        for i in self.divisions:
            if i >= value: break
            pos += 1
        return ((self.divisions[pos] - self.divisions[pos-1]) / 2) + self.divisions[pos-1]
img = misc.imread('test_images/lena_gray_512.png')
(n,m) = img.shape
k = 2
n_bloque = 8
minMaxBloques = []
values = []
for i in range(n_bloque):
    for j in range(n_bloque):
        for ii in range(int(int(n)/int(n_bloque))):
            for jj in range(int(n/n_bloque)):
                values += [img[i*ii][j*jj]]
        minMaxBloques += [(min(values),max(values))]
        distrib = RangeBlock(k,minMaxBloques[-1][0],minMaxBloques[-1][1])
        for ii in range(int(n/n_bloque)):
            for jj in range(int(n/n_bloque)):
                img[i*ii][j*jj] = int(distrib.Quantization(img[i*ii][j*jj]))
print(values)
plt.imshow(img,cmap=plt.cm.gray)
plt.xticks([])
plt.yticks([])
plt.show()
imgor = misc.imread('test_images/lena_gray_512.png')
Sigma=np.sqrt(sum(sum((imgor-img)**2)))/(n*m)
print('Sigma: ',Sigma)
ratio = 2**k + 16/(n_bloque**2)
print('ratio: ',ratio)