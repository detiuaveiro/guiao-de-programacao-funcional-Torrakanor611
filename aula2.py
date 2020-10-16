import math
from functools import reduce
import numpy as np

#Exercicio 4.1
impar = lambda x : not x % 2 == 0

#Exercicio 4.2
positivo = lambda x : x > 0

#Exercicio 4.3
comparar_modulo = lambda x, y : math.fabs(x) < math.fabs(y)

# 
#Exercicio 4.4
cart2pol = lambda x, y : (math.sqrt(x * x + y**2), np.arctan2(y , x))

# print(cart2pol(1, 1))
# print(cart2pol(1, -1))
# print(cart2pol(-1, 1))
# print(cart2pol(-1, -1))


#Exercicio 4.5
# def aux_ex5(f, g, h):
#     return lambda x, y, z : h(f(x,y), g(y,z))
    
ex5 = lambda f, g, h : lambda x, y, z : h(f(x,y), g(y,z))

#Exercicio 4.6
def quantificador_universal(lista, f):
    if lista == []:
        return True
    if f(lista[0]) == False:
        return False
    return quantificador_universal(lista[1:], f)

# return f(lista[0]) and quantificador_universal(lista[1:], f)

# print(quantificador_universal([2,3,4,5,6,7], lambda x : x > 1))
# print(quantificador_universal([2,3,4,5,6,7], lambda x : x < 1))
# print(quantificador_universal([2,3,4,5,6,7], lambda x : x > 9))
# print(quantificador_universal([2,3,4,5,6,7], lambda x : x < 9))

#Exrcício 4.7
def quantificador_existencial(lista, f):
    if lista == []:
        return []
    return f(lista[0]) or quantificador_existencial(lista[1:], f)

#Exercício 4.8
def sub_conjunto(l1, l2):
    assert len(l1) <= len(l2)

    if l1 == []:
        return True
    return (l1[0] in l2) and sub_conjunto(l1[1:], l2)

# print(sub_conjunto([2,3,4], [2,3,4,5,6]))
# print(sub_conjunto([7,8,9], [2,3,4,5,6]))
    
# # tentar com reduce
# #Exercicio 4.9
# def ordem(lista, f):
#     if len(lista) == 1:
#         return lista[0]     # será o último índice da lista inicial

#     m = ordem(lista[1:], f)

#     #return lista[0] if f(lista[0], m) else m

#     if f(lista[0], m):
#         return lista[0]
    
#     return m

#Exercicio 4.9
def ordem(lista, f):
    if len(lista) == 1:
        return lista[0]

    m = lista[0]

    c = ordem(lista[1:], f)

    if f(m, c):
        return m

    return c

# print(ordem([2,3,4,5,6,7], lambda x, y : x < y))
# print(ordem([10,9,8,2,7,8,9,10,11], lambda x, y : x < y))
# print(ordem([10,9,8,6,7,8,9,10,17,18], lambda x, y : x < y))
# print(ordem([10,9,8,2,7,8,9,10,17,18], lambda x, y : x < y))
# print(ordem([-4,8,6,-6,1,-12,1,2,3,7,8], lambda x, y : x < y))


#Exercicio 4.10
def filtrar_ordem(lista, f):
    if len(lista) == 1:
        return lista[0], []

    last = lista[len(lista) - 1]

    c, l1 = filtrar_ordem(lista[:(len(lista) - 1)], f)


    print(c, last, l1)

    if f(c, last):
        return last, l1

    l1.append(last)

    return c, l1

print([1,-1,4,0])
print(filtrar_ordem([1,-1,4,0], lambda x, y: x < y))

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
