def obtener_asientos_ocupados(filas, columnas, asientos):
  asientos_ocupados = []
  for fila in range(filas):
      for columna in range(columnas):
          if asientos[fila][columna] is not None:
              asientos_ocupados.append((fila, columna, asientos[fila][columna]))
  return asientos_ocupados
def ordenar_asientos_por_burbuja(asientos_ocupados):
  n = len(asientos_ocupados)
  for i in range(n):
      for j in range(0, n - i - 1):
          # Compara filas y, si es igual, compara columnas
          if (asientos_ocupados[j][0] > asientos_ocupados[j + 1][0]) or (
              asientos_ocupados[j][0] == asientos_ocupados[j + 1][0] and asientos_ocupados[j][1] > asientos_ocupados[j + 1][1]
          ):
              asientos_ocupados[j], asientos_ocupados[j + 1] = asientos_ocupados[j + 1], asientos_ocupados[j]
  return asientos_ocupados
def mostrar_asientos_ordenados():
  # Provide values for 'filas', 'columnas', and 'asientos' here
  filas = 5 # Example value for 'filas'
  columnas = 3 # Example value for 'columnas'
  asientos = [
      ["A", "B", "C"],
      ["D", "E", "F"],
      ["G", "H", "I"],
      ["J", "K", "L"],
      ["M", "N", "O"]
  ] # Example value for 'asientos'
  asientos_ocupados = obtener_asientos_ocupados(filas, columnas, asientos)  # Call the function with arguments
  asientos_ordenados = ordenar_asientos_por_burbuja(asientos_ocupados)
  print("\nAsientos ocupados ordenados:")
  for fila, columna, pasajero in asientos_ordenados:
      print(f"Fila {fila+1}, Columna {chr(65 + columna)} - {pasajero}")
# Ejemplo de ejecución
mostrar_asientos_ordenados()