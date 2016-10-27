# -*- coding: utf-8 -*-


import math
import random

"""
Dado x en [0,1) dar su representacion en binario, por ejemplo
dec2bin(0.625)='101'
dec2bin(0.0625)='0001'

Dada la representación binaria de un real perteneciente al intervalo [0,1) 
dar su representación en decimal, por ejemplo

bin2dec('101')=0.625
bin2dec('0001')=0.0625

nb número máximo de bits

"""



def dec2bin(x,nb=100):
    ret = ''
    for _ in range(nb):
        x *= 2
        if x == 0:
            break
        if x >=1:
            x -= 1
            ret += '1'
        else:
            ret += '0'
    return ret

def bin2dec(xb):
    ret = 0
    for i in range(len(xb)):
        i += 1
        ret += int(xb[i-1])/2**i
    return ret


print('0.625 = ',dec2bin(0.625))

print('0.0625 = ',dec2bin(0.0625))

print('101 = ',bin2dec('101'))
print ('0001 = ', bin2dec('0001'))
"""
Dada una distribución de probabilidad p(i), i=1..n,
hallar su función distribución:
f(0)=0
f(i)=sum(p(k),k=1..i).
"""

def cdf(p):
    ret = []
    suma = 0.0
    ret.append(suma)
    for prob in sorted(p, reverse = True):
        suma += prob
        ret.append(suma)
    return ret

probabilidades=[0.4,0.3,0.2,0.1]
print(cdf(probabilidades))

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el intervalo (l,u) que representa al mensaje.

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
Arithmetic(mensaje,alfabeto,probabilidades)=0.876 0.8776
"""

def Arithmetic(mensaje,alfabeto,probabilidades):
    funcion = cdf(probabilidades)
    index = alfabeto.index(mensaje[0])
    l = funcion[index]
    u = funcion[index+1]
    for letra in mensaje[1:]:
        diff = u -l
        index = alfabeto.index(letra)
        u = l + diff * funcion[index+1]
        l = l + diff * funcion[index]
    return l,u

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(Arithmetic(mensaje,alfabeto,probabilidades))


"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar la representación binaria de x=r/2**(t) siendo t el menor 
entero tal que 1/2**(t)<l-u, r entero (si es posible par) tal 
que l*2**(t)<=r<u*2**(t)

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
EncodeArithmetic1(mensaje,alfabeto,probabilidades)='111000001'
"""

def int2bin(number):
    if (number == 1):
        return '1'
    else:
        return int2bin(int(number/2)) + str(number%2)

def EncodeArithmetic1(mensaje,alfabeto,probabilidades):
    l,u = Arithmetic(mensaje,alfabeto,probabilidades)
    t = int(math.ceil(math.fabs(math.log2(u-l))))
    print(t)
    #l * 2 ** (t) <= r < u * 2 ** (t) x=r/2**(t); r = x/2**(t)
    lower = int(math.ceil(l*(2**t)))
    upper = int(math.floor(u*(2**t)))
    if upper % 2 == 0: return int2bin(upper>>1)
    elif lower % 2 == 0: return int2bin(lower>>1)
    else: return int2bin(upper)

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(EncodeArithmetic1(mensaje,alfabeto,probabilidades))

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el código que representa el mensaje obtenido a partir de la 
representación binaria de l y u

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
EncodeArithmetic2(mensaje,alfabeto,probabilidades)='111000001'

"""
def getBit(pos,num):
    if (pos >= len(num)): return '0'
    return num[pos]

def EncodeArithmetic2(mensaje,alfabeto,probabilidades):
    l,u = Arithmetic(mensaje,alfabeto,probabilidades)
    lowerBin = dec2bin(l)
    upperBin = dec2bin(u)
    if lowerBin == upperBin: return lowerBin
    else:
        size = len(lowerBin)
        b = len(lowerBin) < len(upperBin)
        if b: size = len(upperBin)
        for i in range(size):
            bit_lower = getBit(i,lowerBin)
            bit_upper = getBit(i,upperBin)
            if bit_lower != bit_upper:
                if b: return upperBin[:i+1]
                else: return lowerBin[:i+1]
    return lowerBin

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(EncodeArithmetic2(mensaje,alfabeto,probabilidades))
"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con su distribución de probabilidad 
dar el mensaje original

code='0'
longitud=4
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
DecodeArithmetic(code,longitud,alfabeto,probabilidades)='aaaa'

code='111000001'
DecodeArithmetic(code,4,alfabeto,probabilidades)='ccda'
DecodeArithmetic(code,5,alfabeto,probabilidades)='ccdab'

"""
def inicioIntervalo(x, puntos):
    for i in range(len(puntos)):
        if x < puntos[i]:
            return int (i-1)

def DecodeArithmetic(code,n,alfabeto,probabilidades):
    mensaje = ''
    funcion = cdf(probabilidades)
    x = bin2dec(code)
    l = 0
    u = 1.0

    for _ in range(n):
        diff = u-l
        funcionEscalada = [l +i *diff for i in funcion]
        point = inicioIntervalo(x,funcionEscalada)
        l = funcionEscalada[point]
        u = funcionEscalada[point+1]
        mensaje += alfabeto[point]
    return mensaje
code='0'
longitud=4
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
print(DecodeArithmetic(code,longitud,alfabeto,probabilidades))
code='111000001'
print(DecodeArithmetic(code,4,alfabeto,probabilidades))
'''
Función que compara la longitud esperada del 
mensaje con la obtenida con la codificación aritmética
'''

def comparacion(mensaje,alfabeto,probabilidades):
    p=1.
    indice=dict([(alfabeto[i],i+1) for i in range(len(alfabeto))])
    for i in range(len(mensaje)):
        p=p*probabilidades[indice[mensaje[i]]-1]
    aux=-math.log(p,2), len(EncodeArithmetic1(mensaje,alfabeto,probabilidades)), len(EncodeArithmetic2(mensaje,alfabeto,probabilidades))
    print('Información y longitudes:',aux)    
    return aux
        
        
'''
Generar 10 mensajes aleatorios M de longitud 10<=n<=20 aleatoria 
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e', codificarlo y compararlas longitudes 
esperadas con las obtenidas.
'''

alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
    Y = []
    for _ in range(k):
        Y +=[random.choice(X)]
    return Y

l_max=20

for _ in range(10):
    n=random.randint(10,l_max)
    L = rd_choice(U, n)
    mensaje = ''
    for x in L:
        mensaje += x
    print('---------- ',mensaje)    
    C = comparacion(mensaje,alfabeto,probabilidades)
    print(C)

    

'''
Generar 10 mensajes aleatorios M de longitud 10<=n<=100 aleatoria 
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.

alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
    Y = []
    for _ in range(k):
        Y +=[random.choice(X)]
    return Y

l_max=100

for _ in range(10):
    n=random.randint(10,l_max)
    L = rd_choice(U, n)
    mensaje = ''
    for x in L:
        mensaje += x
    print('---------- ',mensaje)    
    C = EncodeArithmetic1(mensaje,alfabeto,probabilidades)
    print(C)
'''
