# -*- coding: utf-8 -*-


import random
import numpy as np
import sys

'''
0. Dada una codificación R, construir un diccionario para codificar m2c y otro para decodificar c2m
'''
R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])


'''
1. Definir una función Encode(M, m2c) que, dado un mensaje M y un diccionario 
de codificación m2c, devuelva el mensaje codificado C.
'''

def Encode(M, m2c):
    mensaje = ""
    for letra in M:
        mensaje += m2c[letra]
    return mensaje
    
    
''' 
2. Definir una función Decode(C, m2c) que, dado un mensaje codificado C y un diccionario 
de decodificación c2m, devuelva el mensaje original M.
'''
def GetMax(list):
    max = 0
    for value in list:
        if max < len(value):
            max = len(value)
    return max

def Decode2(M,c2m):
    current = ''
    mensaje = ''
    for simbolo in M:
        current += simbolo
        if current in c2m:
            mensaje += c2m[current]
            current = ''
    return mensaje

def Decode(C,c2m):
    size = GetMax(c2m)
    return DecodeAux(C,c2m,"","",size)

def DecodeAux(C,c2m,Current,PosMessage,MaxSize):
    if C == "" and Current == "":
        return PosMessage
    elif len(Current) > MaxSize:
        return ""
    else:
        if Current in c2m:
            res = DecodeAux(C,c2m,"",PosMessage + c2m[Current],MaxSize)
            if res == "":
                return DecodeAux(C[1:],c2m,Current + C[0],PosMessage,MaxSize)
            else:
                return res
        else:
            if len(C) > 0:
                return DecodeAux(C[1:],c2m,Current + C[0],PosMessage,MaxSize)
            else:
                return ""

#------------------------------------------------------------------------
# Ejemplo 1
#------------------------------------------------------------------------

R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

'''
3. Generar un mensaje aleatorio M de longitud 50 con las frecuencias 
esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''
def GenerateRandomMessage(elements,size,probabilities):
    listedMessage = np.random.choice(elements,size,list(probabilites))
    M = ""
    for elem in listedMessage:
        M += elem
    return M

elements = np.array(['a','b', 'c', 'd', 'e'])
probabilites = np.array([0.5, 0.2, 0.15,0.10,0.05])
M= GenerateRandomMessage(elements,50,probabilites)

C = Encode(M,m2c)
aux = Decode(C,c2m)
if M == aux:
    print('test 3. Ok')
else:
    print('test 3. Failed')

''' 
4. Si 'a', 'b', 'c', 'd', 'e' se codifican inicialmente con un código de 
bloque de 3 bits, hallar la ratio de compresión al utilizar el nuevo código.  
'''

r = 8/3.0
print("ratio: " + str(r))




#------------------------------------------------------------------------
# Ejemplo 2
#------------------------------------------------------------------------
R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
5.
Codificar y decodificar 20 mensajes aleatorios de longitudes también aleatorios.  
Comprobar si los mensajes decodificados coinciden con los originales.
'''

iter = 0
b= True
while iter < 20:
    size = np.random.randint(1,200)
    elements = np.array(['a', 'b', 'c', 'd', 'e'])
    probabilites = np.array([0.2, 0.2, 0.2, 0.2, 0.2])
    M = GenerateRandomMessage(elements, size, probabilites)
    C = Encode(M,m2c)

    D = Decode(C,c2m)
    iter += 1
if b:
    print('test 5. Ok')
else:
    print('test 5. Failed')



#------------------------------------------------------------------------
# Ejemplo 3 
#------------------------------------------------------------------------
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
6. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''

M = 'ae'
C = Encode(M,m2c)
D = Decode(C,c2m)
if M == D:
    print('Test 6.1. Ok')
else:
    print('Test 6.1. Failed')
M = 'be'
C = Encode(M,m2c)
D = Decode(C,c2m)
if M == D:
    print('Test 6.2. Ok')
else:
    print('Test 6.1. Failed')

print('----PRUEBAS-----')

R = [('a','10'), ('b','11'), ('c','111'), ('d','1111')]
'''a. ['00', '01', '100', '101', '110', '111', '1111']
b.

['00', '010', '011', '100', '101', '1100', '1101', '1110', '1111']
c. ['0', '10', '110', '111']
d. ['00', '010', '011', '100', '101', '1100', '1101', '1110', '1111', '11111']'''
# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

mensaje= 'abcd'
C = Encode(mensaje,m2c)
D = Decode(C,c2m)
print(mensaje, ' ', D)
print(D == mensaje)
