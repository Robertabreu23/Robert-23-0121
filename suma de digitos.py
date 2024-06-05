def suma_digitos(numero):
  return sum(int(digito) for digito in str(numero))

def es_primo(n):
  if n <= 1:
      return False
  if n == 2:
      return True
  if n % 2 == 0:
      return False
  for i in range(3, int(n**0.5) + 1, 2):
      if n % i == 0:
          return False
  return True

def mostrar_digitos_separados(numero):
  return list(str(numero))

# Leer dos números enteros
num1 = int(input("Ingresa el primer número entero: "))
num2 = int(input("Ingresa el segundo número entero: "))

# Calcular la diferencia
diferencia = abs(num1 - num2)

# Condición 1: Si la diferencia es par
if diferencia % 2 == 0:
  suma_digitos_num1 = suma_digitos(num1)
  suma_digitos_num2 = suma_digitos(num2)
  print(f"La suma de los dígitos del primer número es: {suma_digitos_num1}")
  print(f"La suma de los dígitos del segundo número es: {suma_digitos_num2}")

# Condición 2: Si la diferencia es un número primo menor que 10
if es_primo(diferencia) and diferencia < 10:
  producto = num1 * num2
  print(f"El producto de los dos números es: {producto}")

# Condición 3: Si la diferencia termina en 4
if str(diferencia).endswith('4'):
  digitos_num1 = mostrar_digitos_separados(num1)
  digitos_num2 = mostrar_digitos_separados(num2)
  print(f"Los dígitos del primer número son: {', '.join(digitos_num1)}")
  print(f"Los dígitos del segundo número son: {', '.join(digitos_num2)}")
