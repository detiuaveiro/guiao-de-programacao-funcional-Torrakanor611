from aula1 import capicua as capi
from aula1 import separar

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


# if __name__ == '__main__':
#     main()