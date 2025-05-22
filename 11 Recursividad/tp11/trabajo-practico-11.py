# Ejercicio 1
def calcula_factoriales(num):
  
  def factorial(num):
    return 1 if num == 1 else num * factorial(num - 1)
  
  print(f"El factorial de los números comprendidos entre 1 y {num} son: ")
  
  for i in range(1, num):
    print(f"{i}! = {factorial(i)}")
  print(f"El factorial del número ingresado({num}!) es: {factorial(num)}.")  

caso = int(input("Ingrese un número para saber su factorial: "))
calcula_factoriales(caso)

# Ejercicio 2
def fibonacci_recursivo(pos):
  
  def calcula_fibonacci(p):  
    return p if p == 0 or p == 1 else calcula_fibonacci(p - 1) + calcula_fibonacci(p - 2)
  
  print(f"El valor de la serie Fibonacci en la posición {pos} es: {calcula_fibonacci(pos)}.")
  print("La serie completa es: ")  
  for i in range(1, pos + 1):
    print(f"{calcula_fibonacci(i)}")

posicion = int(input("Ingrese la posición que desea saber de una serie Fibonacci: "))
fibonacci_recursivo(posicion)

# Ejercicio 3
def potencia_recursiva(numero, potencia):
  return 1 if potencia == 0 else numero * potencia_recursiva(numero, potencia - 1)
    
base = int(input("Ingrese un número para potenciar: "))
exponente = int(input("Ingrese la potencia de la base: "))
print(f"El numero {base}, elevado a la potencia {exponente}, es {potencia_recursiva(base, exponente)}.")

# Ejercicio 4
def binario_recursivo(num):
  return str(num) if num < 2 else binario_recursivo(num // 2) + str(num % 2)

numero = int(input("Ingrese un número decimal para convertirlo a binario: "))

print(f"El número {numero} en binario es: {binario_recursivo(numero)}.")

# Ejercicio 5
entrada = input("Ingresa una palabra para saber si es palíndromo: ")
def es_palindromo(palabra):
  comparador = []
  def compara_recursivo(p):
    if len(p) == 0:
      return 
    comparador.append(p[-1])
    compara_recursivo(p[:-1])
  
  compara_recursivo(palabra)
  comparador = ''.join(comparador)
 
  return True if comparador == entrada else False

es_palindromo(entrada)

if es_palindromo(entrada):
  print(f"Tu palabra {entrada} es palíndromo.")
elif not es_palindromo(entrada):
  print(f"Tu palabra {entrada} NO es palíndromo.")
else:
  print("La entrada que ingresaste no es válida.")

# Ejercicio 6
def suma_digitos(n):
 return n if n <= 9 else n % 10 + suma_digitos(n // 10)
 
numero = int(input("Ingresa un número para saber la suma de sus dígitos: "))

print(f"La suma de los dígitos que componen el número {numero}, es: {suma_digitos(numero)}.")

# Ejercicio 7
def contar_bloques(n):
  return n if n <= 1 else n + contar_bloques(n - 1)
  
nivel_inicial = int(input("Cúantos bloques tiene el nivel inicial de tu pirámide?: "))  

print(f"Necesitarás {contar_bloques(nivel_inicial)} bloques para construir tu pirámide.")

# Ejercicio 8
def contar_digito(numero, digito):
 contador = 0
 def comparador_recursivo(num, dig):
  nonlocal contador
  if num <= 9:
   if num == dig:
    contador += 1
   else:
     return
  else:
   if num % 10 == dig:
    contador += 1
    return comparador_recursivo(num // 10, dig) 
   else:
    return comparador_recursivo(num // 10, dig)

 comparador_recursivo(numero, digito)
 return contador 

entero = int(input("Ingrese un número en el cúal buscar un dígito: "))
parametro = int(input("Ingrese el número que desea saber cuantas veces aparece en el número: "))

print(f"El número {parametro}, se encuentra {contar_digito(entero, parametro)} veces, dentro del número {entero}.")