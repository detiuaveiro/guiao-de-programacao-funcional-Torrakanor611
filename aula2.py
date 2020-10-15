import math

#Exercicio 4.1
impar = lambda x : not x % 2 == 0

#Exercicio 4.2
positivo = lambda x : x > 0

#Exercicio 4.3
comparar_modulo = lambda x, y : math.fabs(x) < math.fabs(y)

#Exercicio 4.4
cart2pol = lambda x, y : (math.sqrt( x * x + y * y ), math.atan(y/x)) 

#Exercicio 4.5
def aux_ex5(f, g, h):
    return lambda x, y, z : h(f(x,y), g(y,z))
    
ex5 = lambda f, g, h : aux_ex5(f, g, h)

#Exercicio 4.6
def quantificador_universal(lista, f):
    pass

#Exercicio 4.9
def ordem(lista, f):
    pass

#Exercicio 4.10
def filtrar_ordem(lista, f):
    pass

#Exercicio 5.2
def ordenar_seleccao(lista, ordem):
    pass
