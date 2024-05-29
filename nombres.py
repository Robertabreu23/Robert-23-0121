#Iteracion sobre la lista de nombres que imprima solamente los nombres que tengan igual o mas de tres vocales.
vocales =["a","e","i","o","u","A","E","I","O","U"]
nombres= input("ingresa un nombre:")
contador = 0
for letra in nombres:
  if letra in vocales:
    contador += 2

if contador >= 3:
    print(nombres)
else:
    print("no hay nombres con 3 o mas vocales")

