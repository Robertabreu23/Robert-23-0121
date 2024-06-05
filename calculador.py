#Hacer una calculadora que permite y sumar y restar
def main():
  while True:
      print("1-Suma")
      print("2-Resta")
      print("3-Multiplicacion")
      print("4-Division")
      print("5-Salir")
      opc = int(input("Ingrese una opcion: "))

      if opc == 1:
          n1 = int(input("Ingrese el primer numero: "))
          n2 = int(input("Ingrese el segundo numero: "))
          print("El resultado de la Suma es:", n1 + n2)
      elif opc == 2:
          n1 = int(input("Ingrese el primer numero: "))
          n2 = int(input("Ingrese el segundo numero: "))
          print("El resultado de la Resta es:", n1 - n2)
      elif opc == 3:
          n1 = int(input("Ingrese el primer numero: "))
          n2 = int(input("Ingrese el segundo numero: "))
          print("El resultado de la Multiplicacion es:", n1 * n2)
      elif opc == 4:
          n1 = int(input("Ingrese el primer numero: "))
          n2 = int(input("Ingrese el segundo numero: "))
          if n2 == 0:
              print("Error: Division por cero")
          else:
              print("El resultado de la Division es:", n1 / n2)
      elif opc == 5:
          print("Adios!!")
          break
      else:
          print("Opcion no valida")

      if opc != 5:
          continuar = input("¿Desea continuar? (S/N): ").upper()
          if continuar == "N":
              break

if __name__ == "__main__":
  main()
