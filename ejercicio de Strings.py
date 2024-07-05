#Leer un texto y realizar las siguientes operaciones:
s1=input("ingrese un texto: ")
#Retornar el texto en mayusculas
print(s1.upper())
#Retornar el texto en minusculas
print(s1.lower())
#Retornar los dos primeros caracteres
print(s1[0:2])
#Retornar la cantidaad de veces que se repite el ultimo caracter
print(s1.count(s1[-1]))
#Retornar el texto invertido
print(s1[::-1])

