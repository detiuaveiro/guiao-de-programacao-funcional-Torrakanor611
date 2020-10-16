import copy
import sys

#Exercicio 1.1
def comprimento(lista):
	if lista == []:
		return 0
	return 1 + comprimento(lista[1:])

#Exercicio 1.2
def soma(lista):
	if lista == []:
		return 0
	return lista[0] + soma(lista[1:]) 
	
#Exercicio 1.3
def existe(lista, elem):
	if lista == []:
		return False
	elif(lista[0] == elem):
		return True
	else:
		return existe(lista[1:], elem)


#Exercicio 1.4
def concat(l1, l2):
	if not l2 == []:
		l1.append(l2[0])
		concat(l1, l2[1:])
	return l1

	# conteúdo original de l1 e l2 destrúido
	# import copy
	# l3 = copy.deepcopy(l1) p.e.

#Exercicio 1.5
def inverte(lista):
	if lista == []:
		return []
	return inverte(lista[1:]) + [lista[0]]

#Exercicio 1.6
def capicua(lista):
	if len(lista) == 1 or lista == []:
		return True
	if lista[0] == lista[(len(lista) -1)]:
		return capicua(lista[1:len(lista) - 1])
	else:
		return False

#Exercicio 1.7
def explode(lista):
	if lista[1] == []:
		return lista[0]

	lista[0].append(lista[1][0])

	lista = [lista[0], lista[1][1:]]
	return explode(lista)

#Exercicio 1.8
def substitui(lista, original, novo):
	if lista == []:
		return lista

	if lista[0] == original:
		lista[0] = novo

	return [lista[0]] + substitui(lista[1:], original, novo)
	
	

#Exercicio 1.9
def junta_ordenado(lista1, lista2):

	x = []
	y = []

	if not lista1 == []:
		x = [lista1[0]]

	if not lista2 == []:
		y = [lista2[0]]

	if x == [] and y == []:
		return []

	return x + y + junta_ordenado(lista1[1:], lista2[1:])

# #2.1
# def separar(lista):
# 	if not lista == []:
# 		if

# #Exercicio 2.1
# def separar(lista):
# 	if lista == []:
# 		return []

# 	lista = separar_aux(lista)
# 	# print(lista)

# 	l1 = []
# 	l2 = []

# 	for i in range(0, len(lista)):
# 		# print(i)
# 		if i % 2 == 0:
# 			l1.append(lista[i])
# 		else:
# 			l2.append(lista[i])
	
# 	return(l1, l2)

# def separar_aux(lista):
# 	if lista == []:
# 		return []
# 	return [lista[0][0]] + [lista[0][1]] + separar_aux(lista[1:])

#Exercicio 2.1
def separar(lista):
	if lista == []:
		return ([], [])

	tuplo = lista[len(lista) - 1]

	l1, l2 = separar(lista[:(len(lista) - 1)])

	l1.append(tuplo[0])
	l2.append(tuplo[1])

	return (l1, l2)


# #Exercicio 2.2
# def remove_e_conta(lista, elem):
# 	# if lista == []:
# 	# 	return []
	
# 	# lista_aux = copy.deepcopy(lista)
# 	# count = 0

# 	# remove_e_conta_aux(lista, lista_aux, elem, count)

# 	# return (lista_aux, count)
# 	pass

# def remove_e_conta_aux(lista, lista_aux, elem, count):
# 	if lista == []:
# 		return []
	
# 	if lista[0] == elem:
# 		lista_aux.remove(lista[0])
# 		count = count + 1

# 	remove_e_conta_aux(lista[1:], lista_aux, elem, count)

# count = 0

# def remove_e_conta(lista, elem):

# 	global count

# 	if not elem in lista:
# 		return (lista, count)
# 	else:
# 		lista.remove(elem)
# 		#print(lista)
# 		count = count +1
# 		return remove_e_conta(lista, elem)

#Exercicio 2.2
def remove_e_conta(lista, elem):
	if lista == []:
		return [], 0

	value = lista[len(lista) - 1]

	lista, count = remove_e_conta(lista[:len(lista) - 1], elem)

	if value == elem:
		count = count + 1
		return (lista, count)
	else:
		lista.append(value)
		return (lista, count)


#Exercicio 3.1
def cabeca(lista):
	if lista == [] or not type(lista) == list:
		return None
	elif len(lista) == 1:
		return lista[0]
	else:
		return cabeca(lista[:len(lista) - 1])

# print(cabeca([2,3,4,5,6,7]))

#Exercicio 3.2
def cauda(lista):
	return lista[:lista[:len(lista) - 1]]

#Exercicio 3.3
def juntar(l1, l2):
	if not len(l1) == len(l2) or not type(l1) == list or not type(l2) == list:
		return None

	if l1 == [] or l2 == []:
		return []

	v1 = l1[len(l1) - 1]
	v2 = l2[len(l2) - 1]

	lista = juntar(l1[:len(l1) - 1], l2[:len(l2) - 1])

	lista.append((v1, v2))

	return lista

# print(juntar([2,3,4,5,6], [2,9,4,9,6]))

#Exercicio 3.4
def menor(lista):
	if not type(lista) == list or lista == []:
		return None

	if len(lista) == 1:
		min = lista[0]
		return min

	value = lista[0]

	min = menor(lista[1:])

	if value < min:
		min = value

	return min

# print(menor([]))
 
#Exercicio 3.6
def max_min(lista):
	if not type(lista) == list or lista == []:
		return None

	# first value of list is consecutive the 1st min and max
	if len(lista) == 1:
		return (lista[0], lista[0])

	aux_min = lista[0]
	aux_max = lista[0]

	min, max = max_min(lista[1:])

	if aux_max > max:
		max = aux_max
	if aux_min < min:
		min = aux_min

	return (min, max)

# print(max_min([1,2,3,4,5567,3, -5, 8]))
