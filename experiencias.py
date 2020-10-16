from aula1 import capicua as capi
from aula1 import separar, cabeca
from aula2 import comparar_modulo
from functools import reduce


# def main():
lista = [1,2,3,4,5]

print(lista[0])
print(len(lista))
print(lista[3])
print(lista[(len(lista) -1)])

print(capi([1,2,3,4,3,2,1]))
print(capi([1,2,3,3,2,1]))
print(capi([1,2,3,4,5,2,1]))
print(capi([1,2,3,2,2,1]))

lista = [(1,'a'), (2,'b'), (3,'c')]

print(lista[1][0])
print(lista[1][1])

print(lista[1:])

separar(lista)

print(cabeca([2,3,4,5,5,6,7,8]))

print(comparar_modulo(34, 3))

print("----------------------//------------------")

def add(x, y):
    return x < y

list = [2, 4, 7, 3]
print(reduce(add, list))