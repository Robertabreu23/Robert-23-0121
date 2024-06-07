#Calcular el indice de masa corporal
print("Seleccione su unidad de peso")
print("1. Kilogramos (Kg)")
print("2. Libras (Lbs)")
unidad_peso = int(input("Ingrese su unidad de peso: "))

if unidad_peso == 1:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    imc = peso / (altura ** 2)
    print("Su índice de masa corporal es: ", round(imc, 2))

elif unidad_peso == 2:
    peso_libras = float(input("Ingrese su peso en libras: "))
    altura = float(input("Ingrese su altura en metros: "))
    peso_en_kg = peso_libras / 2.2046
    imc = peso_en_kg / (altura ** 2)
    print("Su índice de masa corporal es: ", round(imc, 2))

else:
    print("Unidad de peso no válida. Por favor, ingrese 1 para Kg o 2 para Lbs.")
