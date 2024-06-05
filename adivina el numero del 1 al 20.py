#adivina el numero del 1 al 20 y diga caliente si se acerca y frio si se aleja
import random


numero_secreto = random.randint(1, 20)

print("Bienvenido al juego de adivinar un número!")
print("Estoy pensando en un número entre 1 y 20.")

adivinanza_previo = 0  

while True:

    adivinanza = int(input("Adivina el número: "))


    if adivinanza == numero_secreto:
        print("¡Felicidades! Adivinaste el número correctamente.")
        break


    if adivinanza_previo == 0:  
        if abs(adivinanza - numero_secreto) < 10:  
            print("Caliente! Estás cerca del número secreto.")
        else:
            print("Frio! Te alejas del número secreto.")
    elif abs(adivinanza - numero_secreto) < abs(adivinanza_previo - numero_secreto):
        print("Caliente! Estás cerca del número secreto.")
    else:
        print("Frio! Te alejas del número secreto.")


    adivinanza_previo = adivinanza