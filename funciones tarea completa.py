#Funcion de saludo
print("Funcion de saludo")
def diHola():
  nombre=(input("Ingresa tu nombre: "))
  print("Hola", nombre, '\n')

diHola()
# Funcion de suma

print( "Funcion de suma")
def suma():
  suma=a+b
  print("La suma es: ", suma, '\n')  
a = float(input("Ingresa un numero: "))
b = float(input("Ingresa otro numero: "))
suma()

print("Funcion de area de rectangulo")
#funcion area de un rectangulo
def area_rectangulo():
  area=base*altura
  print("El area del rectangulo es: ",area, '\n')
base=float(input("Ingresa la base del rectangulo: "))
altura=float(input("Ingresa la altura del rectangulo: "))
area_rectangulo()

print("Funcion par o impar")
#Número Par o Impar
def par_impar():
  numero=int(input("Ingresa un numero: "))
  if numero % 2 == 0:
    print("El numero es par" '\n')
  else:
    print("El numero es impar" '\n')
par_impar()

print("Conversión de Grados Celsius a Fahrenheit")
#Conversión de Grados Celsius a Fahrenheit
def celsius_fahrenheit():
  celsius=float(input("Ingresa los grados celsius: "))
  fahrenheit=(celsius*9/5)+32
  print("Los grados fahrenheit son: ", fahrenheit, '\n')
celsius_fahrenheit()

print("Máximo de Tres Números")
#Máximo de Tres Números
def maximo_tres_numeros():
  numero1=float(input("Ingresa el primer numero: "))
  numero2=float(input("Ingresa el segundo numero: "))
  numero3=float(input("Ingresa el tercer numero: "))
  if numero1>numero2 and numero1>numero3:
    print("El numero mayor es: ", numero1, '\n')
  elif numero2>numero1 and numero2>numero3:
    print("El numero mayor es: ", numero2, '\n')
  else:
    print("El numero mayor es: ", numero3, '\n')
maximo_tres_numeros()

print("Palíndromo")
#Palíndromo
def palindromo():
  palabra=input("Ingresa una palabra: ")
  palabra_invertida=palabra[::-1]
  if palabra==palabra_invertida:
    print("La palabra es palindromo" '\n')
  else:
    print("La palabra no es palindromo" '\n')
palindromo()

print("Factorial")
#Factorial
def factorial():
  numero=int(input("Ingresa un numero: "))
  factorial=1
  for i in range(1, numero+1):
    factorial=factorial*i
  print("El factorial es: ", factorial, '\n')
factorial()

print("Contar vocales")
#Contar vocales
def contar_vocales():
  palabra=input("Ingresa una palabra: ")
  vocales=0
  for letra in palabra:
    if letra.lower() in "aeiou":
      vocales+=1
  print("La palabra tiene", vocales, "vocales" '\n')
contar_vocales()

print("Numeros Primos")
#Numeros Primos
def numeros_primos():
  numero=int(input("Ingresa un numero: "))
  es_primo=True
  for i in range(2, numero):
    if numero % i == 0:
      es_primo=False
      break
  if es_primo:
    print("El numero es primo" '\n')
  else:
    print("El numero no es primo" '\n')
numeros_primos()