#Listas, Tuplas y Diccionario

lista = [10, 20, 30, 40, 50]

print("Elemento en índice 2 de la lista:", lista[2])  # Output: 30

lista[1] = 25


print("Lista actualizada:", lista)  # Output: [10, 25, 30, 40, 50]


tupla = (100, 200, 300, 400)

print("Elemento en índice 0 de la tupla:", tupla[0])  # Output: 100


lista_tupla = list(tupla)
lista_tupla[1] = 250
tupla_modificada = tuple(lista_tupla)

print("Tupla modificada:", tupla_modificada)  # Output: (100, 250, 300, 400)

diccionario = {'a': 1, 'b': 2, 'c': 3}


print("Valor asociado a 'b' en el diccionario:", diccionario['b'])  # Output: 2


diccionario['c'] = 30


print("Diccionario actualizado:", diccionario)  # Output: {'a': 1, 'b': 2, 'c': 30}