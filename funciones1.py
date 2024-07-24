#funcion de saludo
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

#funcion area de un rectangulo
def area_rectangulo():
  area=base*altura
  print("El area del rectangulo es: ",area, '\n')
base=float(input("Ingresa la base del rectangulo: "))
altura=float(input("Ingresa la altura del rectangulo: "))
area_rectangulo()
