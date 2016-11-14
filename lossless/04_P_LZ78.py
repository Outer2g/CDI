# -*- coding: utf-8 -*-


"""
Dado un mensaje dar su codificación  usando el
algoritmo LZ78


mensaje='wabba wabba wabba wabba woo woo woo'
LZ78Code(mensaje)=[[0, 'w'], [0, 'a'], [0, 'b'], [3, 'a'], 
                   [0, ' '], [1, 'a'], [3, 'b'], [2, ' '], 
                   [6, 'b'], [4, ' '], [9, 'b'], [8, 'w'], 
                   [0, 'o'], [13, ' '], [1, 'o'], [14, 'w'], 
                   [13, 'o'], [0, 'EOF']]
  
"""
def LZ78Code(mensaje):
    Dicc = ['']
    ret = []
    current = ''
    for letra in mensaje:
        current += letra
        if not current in Dicc:
            if len(current) == 1: Dicc += [current]; ret+=[[0,current]]
            else: Dicc += [current]; ret += [[Dicc.index(current[:-1]),current[-1:]]]
            current = ''
    if current != '': ret += [[Dicc.index(current),'EOF']]
    else: ret += [[0,'EOF']]
    return ret
"""
Dado un mensaje codificado con el algoritmo LZ78 hallar el mensaje 
correspondiente 

code=[[0, 'm'], [0, 'i'], [0, 's'], [3, 'i'], [3, 's'], 
      [2, 'p'], [0, 'p'], [2, ' '], [1, 'i'], [5, 'i'], 
      [10, 'p'], [7, 'i'], [0, ' '], [0, 'r'], [2, 'v'], 
      [0, 'e'], [14, 'EOF']]

LZ78Decode(mensaje)='mississippi mississippi river'
"""    
def LZ78Decode(codigo):
    mensaje = ''
    dicc = ['']
    for elem in codigo:
        current = dicc[elem[0]] + elem[1]
        dicc += [current]
        mensaje += current
    return mensaje[:-3]
    

print('----------PRUEBAS-----------')
code = [[0, 'E'], [0, 'n'], [0, ' '], [0, 'm'], [0, 'u'], [0, 'c'], [0, 'h'], [0, 'a'], [0, 's'], [3, 'd'], [0, 'e'], [3, 'l'], [8, 's'], [3, 'c'], [0, 'i'], [0, 'v'], [15, 'l'], [15, 'z'], [8, 'c'], [15, 'o'], [2, 'e'], [9, ' '], [4, 'á'], [22, 't'], [0, 'r'], [8, 'n'], [0, 'q'], [5, 'i'], [0, 'l'], [13, ' '], [0, 'd'], [11, 'l'], [3, 'm'], [8, 'r'], [0, 'g'], [11, 'n'], [3, 'o'], [25, 'i'], [36, 't'], [8, 'l'], [10, 'e'], [12, 'a'], [3, 'g'], [40, 'a'], [0, 'x'], [15, 'a'], [42, ' '], [0, '"'], [0, 'G'], [5, 'í'], [8, ' '], [31, 'e'], [29, ' '], [8, 'u'], [0, 't'], [0, 'o'], [11, 's'], [55, 'o'], [0, 'p'], [15, 's'], [55, 'a'], [43, 'a'], [29, 'á'], [6, 't'], [15, 'c'], [56, '"'], [3, 'y'], [51, 'h'], [51, 's'], [5, 's'], [55, 'i'], [55, 'u'], [15, 'd'], [56, ' '], [51, 'l'], [51, 'g'], [25, 'a'], [2, ' '], [48, 'E'], [2, 'c'], [65, 'l'], [56, 'p'], [11, 'd'], [46, ' '], [35, 'a'], [63, 'c'], [71, 'c'], [8, '"'], [14, 'o'], [4, 'o'], [47, 'f'], [5, 'e'], [2, 't'], [11, ' '], [25, 'e'], [6, 'o'], [2, 'o'], [6, 'i'], [31, 'a'], [41, ' '], [58, 'd'], [74, 'e'], [53, 'c'], [56, 'n'], [56, 'c'], [15, 'm'], [15, 'e'], [93, 'o'], [67, ' '], [29, 'a'], [3, 's'], [8, 'b'], [73, 'u'], [25, 'í'], [8, ','], [3, 'p'], [56, 'r'], [27, 'u'], [94, 's'], [15, ' '], [0, 'b'], [107, 'n'], [3, 'i'], [80, 'u'], [25, 'r'], [94, 'e'], [78, 'm'], [5, 'c'], [7, 'a'], [22, 'o'], [4, 'i'], [9, 'i'], [104, 'e'], [22, 'y'], [89, 'n'], [71, 'e'], [21, ' '], [112, 'u'], [2, 'd'], [26, 't'], [57, ' '], [7, 'e'], [6, 'h'], [56, 's'], [100, 'a'], [5, 't'], [39, 'i'], [98, 'd'], [8, 'd'], [10, 'u'], [31, 'o'], [9, 'a'], [0, ','], [111, 'u'], [59, 'e'], [77, ' '], [75, 'a'], [111, 'e'], [35, 'u'], [139, 'a'], [37, 'b'], [77, ','], [33, 'á'], [22, 'a'], [93, 'i'], [159, 'a'], [109, 'p'], [25, 'o'], [152, 'i'], [6, 'a'], [153, ' '], [36, ' '], [151, 's'], [3, 'a'], [9, 'p'], [11, 'c'], [58, 's'], [123, 'm'], [59, 'o'], [25, 't'], [140, 'e'], [9, '.'], [3, 'E'], [78, 'p'], [38, 'm'], [11, 'r'], [12, 'u'], [85, 'r'], [171, 'e'], [22, 'u'], [184, 'o'], [96, ' '], [23, 's'], [3, 'b'], [34, 'a'], [61, ';'], [187, 'e'], [35, 'o'], [171, 'g'], [77, 'b'], [149, 'a'], [3, 'e'], [78, 'l'], [51, 'p'], [117, 't'], [201, ' '], [96, 'n'], [111, 'i'], [4, 'p'], [0, 'á'], [87, 'a'], [22, 'l'], [11, 't'], [77, 's'], [43, 'r'], [26, 'd'], [57, ','], [37, 's'], [55, 'e'], [93, 'a'], [47, 'l'], [11, 'y'], [36, 'd'], [51, 'N'], [0, 'O'], [3, 'S'], [1, ' '], [0, 'A'], [0, 'S'], [0, 'U'], [229, 'T'], [1, '.'], [0, 'EOF']]
mensaje = LZ78Decode(code)
print(mensaje)
mensaje = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print(len(mensaje))
c = LZ78Code(mensaje)
print(c,'l = ', len(c))
'''mensaje='wabba wabba wabba wabba woo woo woo'
mensaje_codificado=LZ78Code(mensaje)
print('Código: ',mensaje_codificado)   
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print('Código: ',mensaje_codificado)   
print(mensaje)
print(mensaje_recuperado)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

mensaje='mississipi mississipi' 
mensaje_codificado=LZ78Code(mensaje)
print('Código: ',mensaje_codificado)   
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print('Código: ',mensaje_codificado)   
print(mensaje)
print(mensaje_recuperado)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

import time
bits_indice=12
start_time = time.clock()
mensaje_codificado=LZ78Code(mensaje)
print (time.clock() - start_time, "seconds CODE")
start_time = time.clock()
mensaje_recuperado=LZ78Decode(mensaje_codificado)
print (time.clock() - start_time, "seconds DECODE")
ratio_compresion=8*len(mensaje)/((bits_indice+8)*len(mensaje_codificado))
print(len(mensaje_codificado),ratio_compresion)
if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        print(len(mensaje),len(mensaje_recuperado))
        print(mensaje[-5:],mensaje_recuperado[-5:])
else: print('Todo bien')'''




    
