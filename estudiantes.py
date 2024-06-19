#Hacer un programa que calcule el promedio de notas de un estudiante, que pida nombre y matricula y no de un valor negativo que indique si quiere colocar otro estudiante
estudiantes = []

while True:

    nombre = input("Ingrese el nombre del estudiante: ")
    matricula = input("Ingrese la matrícula del estudiante: ")

    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i}: "))
                if nota < 0:
                    print("La nota debe ser negativa. Intente de nuevo.")
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    promedio = sum(notas) / 4
    estudiantes.append((nombre, matricula, promedio))
    otro = input("¿Desea ingresar otro estudiante? (si/no): ")
    if otro != 'si':
        break
print("Promedios de los estudiantes:")
for nombre, matricula, promedio in estudiantes:
    print(f"Nombre: {nombre}, Matrícula: {matricula}, Promedio: {promedio:.2f}")

Salir= input("¿Desea salir? (si/no): ")
if Salir != 'si':
  print("Gracias por preferirnos")
