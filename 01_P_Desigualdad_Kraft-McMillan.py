# -*- coding: utf-8 -*-
"""

"""

'''
Dada la lista L de longitudes de las palabras de un código 
r-ario, decidir si pueden definir un código.

'''

def  kraft1(L, r=2):
    suma = 0
    for longitud in L:
        den = r**longitud
        suma += 1/den
    return suma <= 1


'''
Dada la lista L de longitudes de las palabras de un código 
r-ario, calcular el máximo número de palabras de longitud 
máxima, max(L), que se pueden añadir y seguir siendo un código.

'''

def  kraft2(L, r=2):
    suma = 0
    extras = 0
    for longitud in L:
        den = r**longitud
        suma += 1/den
    maxim = max(L)
    while suma + 1/(r**maxim) <= 1:
        extras +=1
        suma += 1/(r**maxim)
    return extras


'''
Dada la lista L de longitudes de las palabras de un  
código r-ario, calcular el máximo número de palabras 
de longitud Ln, que se pueden añadir y seguir siendo 
un código.
'''

def  kraft3(L, Ln, r=2):
    suma = 0
    extras = 0
    for longitud in L:
        den = r ** longitud
        suma += 1 / den
    while suma + 1 / (r ** Ln) <= 1:
        extras += 1
        suma += 1 / (r ** Ln)
    return extras



'''
Dada la lista L de longitudes de las palabras de un  
código r-ario, hallar un código prefijo con palabras 
con dichas longiutudes
'''
def Code(L,r=2):
    pass





'''
Ejemplo
'''

L=[1,3,5,5,10,3,5,7,8,9,9,2,2,2]
print(sorted(L),' codigo final:',Code(L,3))
print(kraft1(L))
print(kraft2(L))
print(kraft3(L,2))