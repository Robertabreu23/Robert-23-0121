#Tuplas operaaciones
def suma_lista(lista):
  suma = 0
  for elemento in lista:
      suma += elemento
  return suma

mi_lista = [1, 2, 3, 4, 5]
resultado_suma = suma_lista(mi_lista)
print("La suma de los elementos en la lista es:", resultado_suma)
