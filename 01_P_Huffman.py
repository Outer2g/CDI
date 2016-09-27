# -*- coding: utf-8 -*-
"""

"""

#from cdi20152016Q1 import *
import math

'''
Dada una distribucion de probabilidad, hallar un código de Huffman asociado
'''
class Tree:
    def __init__(self,data,left,right):
        self.left = left
        self.right = right
        self.data = data
    def printTree(self):
        if self.left != None: self.left.printTree()
        print('prob: ' + str(self.data))
        if self.right != None: self.right.printTree()

    def produceCode(self,current,list):
        if self.data == 1:
            self.left.produceCode('0',list)
            self.right.produceCode('1',list)
            return list
        if self.left != None and self.right !=None:
            self.left.produceCode(current + '0',list)
            self.right.produceCode(current + '1',list)
        else:
            list.append((self.data,current))
    def produceCodeTuple(self,current,list):
        if self.data == 1:
            self.left.produceCodeTuple('0',list)
            self.right.produceCodeTuple('1',list)
            return list
        if self.left != None and self.right !=None:
            self.left.produceCodeTuple(current + '0',list)
            self.right.produceCodeTuple(current + '1',list)
        else:
            list.append((self.data[0],current))


def Huffman(p):
    #asuming q = 2
    treeList = []
    #build trees
    for prob in sorted(p):
        arbol = Tree(prob,None,None)
        treeList.append(arbol)
    #get pairs of trees, and treat them
    while len(treeList) != 1:
        a1 = treeList[0]
        a2 = treeList[1]
        treeList = treeList[2:]
        aux = Tree(a1.data + a2.data,a1,a2)
        treeList.append(aux)
        treeList.sort(key=lambda x: x.data)
    list = []
    treeList[0].produceCode('',list)
    codigo = list
    return codigo

def H1(p):
    suma = 0
    for prob in p:
        if prob > 0:
            suma += prob * math.log(1/prob,2)
    return suma

def LongitudMedia(C,p):
    media = 0
    for pair in C:
        media += pair[0] * len(pair[1])
    return media

'''
Dada la ddp p=[0.80,0.1,0.05,0.05], hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

p=[0.80,0.1,0.05,0.05]
code = Huffman(p)
print('Code: ',code,' entropia: ',H1(p),' longitud media: ',LongitudMedia(code,p))


'''
Dada la ddp p=[1/n,..../1/n] con n=2**8, hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

n=2**8
p=[1/n for _ in range(n)]
code = Huffman(p)
print('Code2: ',code,'\nentropia: ',H1(p),' longitud media: ',LongitudMedia(code,p))





'''
Dado un mensaje hallar la tabla de frecuencia de los caracteres que lo componen
'''
def tablaFrecuencias(mensaje):
    size = 0
    apariciones = {}
    for letra in mensaje:
        size += 1
        if letra in apariciones:
           apariciones[letra] += 1
        else:
         apariciones[letra] = 1
    for key in apariciones:
        apariciones[key] = apariciones[key] / size
    return apariciones

'''
Definir una función que codifique un mensaje utilizando un código de Huffman 
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''
def HuffmanTuples(p):
    #asuming q = 2
    treeList = []
    #build trees
    for prob in sorted(p,key= lambda x: x[1]):
        arbol = Tree(prob,None,None)
        treeList.append(arbol)
    #get pairs of trees, and treat them
    while len(treeList) != 1:
        a1 = treeList[0]
        a2 = treeList[1]
        treeList = treeList[2:]
        auxData = (a1.data[0]+a2.data[0],+a1.data[1]+a2.data[1])
        aux = Tree(auxData,a1,a2)
        treeList.append(aux)
        treeList.sort(key=lambda x: x.data[1])
    codigo = []
    treeList[0].produceCodeTuple('',codigo)
    return codigo
#from delivery one
def Encode(M, m2c):
    mensaje = ""
    for letra in M:
        mensaje += m2c[letra]
    return mensaje

def EncodeHuffman(mensaje_a_codificar):
    p = tablaFrecuencias(mensaje_a_codificar)
    code = HuffmanTuples(p.items())
    m2c = dict(code)
    return Encode(mensaje_a_codificar,m2c),m2c

def Decode(M,c2m):
    current = ''
    mensaje = ''
    for simbolo in M:
        current += simbolo
        if current in c2m:
            mensaje += c2m[current]
            current = ''
    return mensaje
    
def DecodeHuffman(mensaje_codificado,m2c):
    # decoding dictionary
    c2m = dict([(c, m) for m, c in m2c.items()])
    return Decode(mensaje_codificado,c2m)
    #return mensaje_decodificado
        

'''
Ejemplo
'''

mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
mensaje_codificado, m2c=EncodeHuffman(mensaje)
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c)
print(mensaje_recuperado)
ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
print(ratio_compresion)
