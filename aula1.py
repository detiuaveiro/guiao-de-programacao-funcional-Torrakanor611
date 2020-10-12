import copy

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

#Exercicio 2.1
def separar(lista):
	if lista == []:
		return []

	lista = separar_aux(lista)
	# print(lista)

	l1 = []
	l2 = []

	for i in range(0, len(lista)):
		# print(i)
		if i % 2 == 0:
			l1.append(lista[i])
		else:
			l2.append(lista[i])
	
	return(l1, l2)

def separar_aux(lista):
	if lista == []:
		return []
	return [lista[0][0]] + [lista[0][1]] + separar_aux(lista[1:])


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

count = 0

def remove_e_conta(lista, elem):

	global count

	if not elem in lista:
		return (lista, count)
	else:
		lista.remove(elem)
		#print(lista)
		count = count +1
		return remove_e_conta(lista, elem)

#Exercicio 3.1
def cabeca(lista):
	pass

#Exercicio 3.2
def cauda(lista):
	pass

#Exercicio 3.3
def juntar(l1, l2):
    pass

#Exercicio 3.4
def menor(lista):
	pass

#Exercicio 3.6
def max_min(lista):
	pass
