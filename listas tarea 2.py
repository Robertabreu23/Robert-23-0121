#1.       Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número leído.
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
max_num = max(numeros)
pos_max_num = numeros.index(max_num)
print(f"El mayor número es {max_num} y se encuentra en la posición {pos_max_num}.")

#2.       Leer 10 enteros, almacenarlos en una lista y determinar en qué posición de del arreglo está el mayor número par leído.
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
numeros_pares = [num for num in numeros if num % 2 == 0]
if numeros_pares:
    max_par = max(numeros_pares)
    pos_max_par = numeros.index(max_par)
    print(f"El mayor número par es {max_par} y se encuentra en la posición {pos_max_par}.")
else:
    print("No hay números pares en la lista.")

#3.       Leer 10 enteros, almacenarlos en una lista y determinar en qué posición del arreglo está el mayor número primo leído.
def es_primo(num):
  if num < 2:
      return False
  for i in range(2, int(num**0.5) + 1):
      if num % i == 0:
          return False
  return True

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
numeros_primos = [num for num in numeros if es_primo(num)]
if numeros_primos:
  max_primo = max(numeros_primos)
  pos_max_primo = numeros.index(max_primo)
  print(f"El mayor número primo es {max_primo} y se encuentra en la posición {pos_max_primo}.")
else:
  print("No hay números primos en la lista.")

#4.       Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números de los almacenados en dicho arreglo comienzan en dígito primo
digitos_primos = {'2', '3', '5', '7'}

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
contador = sum(1 for num in numeros if str(num)[0] in digitos_primos)
print(f"Hay {contador} números que comienzan con un dígito primo.")

#5.       Leer 10 números enteros, almacenarlos en una lista y determinar en qué posición se encuentra el número primo con mayor cantidad de dígitos pares.
def contar_digitos_pares(num):
  return sum(1 for digit in str(num) if int(digit) % 2 == 0)

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
numeros_primos = [num for num in numeros if es_primo(num)]

if numeros_primos:
  primo_con_mas_pares = max(numeros_primos, key=contar_digitos_pares)
  pos_primo_con_mas_pares = numeros.index(primo_con_mas_pares)
  print(f"El número primo con más dígitos pares es {primo_con_mas_pares} y se encuentra en la posición {pos_primo_con_mas_pares}.")
else:
  print("No hay números primos en la lista.")

#6.       Leer 10 números enteros, almacenarlos en una lista y determinar en qué posiciones se encuentran los números con más de 3 dígitos
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
posiciones = [i for i, num in enumerate(numeros) if len(str(abs(num))) > 3]
print(f"Las posiciones de los números con más de 3 dígitos son: {posiciones}.")

#7.       Leer 10 números enteros, almacenarlos en una lista y determinar a cuánto es igual el promedio entero de los datos de la lista
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
promedio = sum(numeros) // len(numeros)
print(f"El promedio entero de los datos de la lista es {promedio}.")

#8.       Leer 10 números enteros, almacenarlos en una lista y determinar cuántos números negativos hay.
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
contador_negativos = sum(1 for num in numeros if num < 0)
print(f"Hay {contador_negativos} números negativos en la lista.")

#9.       Leer 10 números enteros, almacenarlos en una lista y calcular la factorial a cada uno de los números leídos almacenándolos en otra lista
from math import factorial

numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
factoriales = [factorial(num) for num in numeros]
print(f"Los factoriales de los números ingresados son: {factoriales}.")

#10.   Leer 10 números enteros, almacenarlos en una lista. Luego leer un entero y determinar cuántos divisores exactos tiene este último número entre los valores almacenados en la lista.
numeros = [int(input(f"Ingrese el número {i+1}: ")) for i in range(10)]
numero_a_verificar = int(input("Ingrese el número a verificar: "))
divisores_exactos = sum(1 for num in numeros if numero_a_verificar % num == 0)
print(f"El número {numero_a_verificar} tiene {divisores_exactos} divisores exactos en la lista.")

