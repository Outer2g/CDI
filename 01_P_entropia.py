# -*- coding: utf-8 -*-
"""

"""
import math
import numpy as np
import matplotlib.pyplot as plt


'''
Dada una lista p, decidir si es una distribución de probabilidad (ddp)
0<=p[i]<=1, sum(p[i])=1.
'''
def es_ddp(p,tolerancia=10**(-5)):
    suma = 0
    for prob in p:
        suma += prob
    return (suma + tolerancia >= 1) and (suma - tolerancia <= 1)

'''
Dado un código C y una ddp p, hallar la longitud media del código.
'''

def LongitudMedia(C,p):
    media = 0
    for i in range(len(C)):
        media += len(C[i]) * p[i]
    return media
    
'''
Dada una ddp p, hallar su entropía.
'''
def H1(p):
    suma = 0
    for prob in p:
        if prob > 0:
            suma += prob * math.log(1/prob,2)
    return suma

'''
Dada una lista de frecuencias n, hallar su entropía.
'''
def H2(n):
    total = 0
    for elem in n:
        total += elem
    suma = 0
    for elem in n:
        prob = elem/total
        if prob > 0:
            suma += prob * math.log(1/prob,2)
    return suma



'''
Ejemplos
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.5,0.1,0.1,0.1,0.1,0.1,0]
n=[5,2,1,1,1]

print(es_ddp(p))
print('longitud media: ' + str(LongitudMedia(C,p)))
print(H1(p))
print(H2(n))
print(LongitudMedia(C,p))



'''
Dibujar H(p,1-p)
'''
def holi():
    x = []
    y = []
    paso = 0.01
    for p in np.arrange(0,1.0,paso):
        x.append(p)
        y.append(H1([p,1-p]))
    plt.plot(x,y,'r-',l2 = 2)
    plt.show()


'''
Hallar aproximadamente el máximo de  H(p,q,1-p-q)
'''



