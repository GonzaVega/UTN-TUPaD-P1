#Ejercicio 1
for i in range(101):
  print(i)

#Ejercicio 2
numero = int(input("Ingrese un número: "))
numero = str(numero)
acumulador = 0

for i in range(len(numero)):
  acumulador += 1

print(f"El número ingresado tiene {acumulador} dígitos")
#Debido a que se esta tratando el tema estructuras repetitivas se construye la solución así, pero luego de convertir a numero en un iterable, podría haber hecho: print(f"El número ingresado tiene {len(numero)} dígitos.")

#Ejercicio 3
numero_inicial = int(input("Ingrese el primer número:"))
numero_final = int(input("Ingrese el segundo número:"))
acumulador = 0

if numero_inicial < numero_final:
  for i in range(numero_inicial + 1, numero_final):
   acumulador += i
elif numero_inicial > numero_final:
  for i in range(numero_final + 1, numero_inicial):
   acumulador += i
else:
  print("Ingresó el mismo número en ambas ocasiones")

print(f"La suma de todos los números comprendidos entre los ingresados es: {acumulador}")

#Ejercicio 4
numero = int(input("Ingrese un número: "))
acumulador = 0

while numero != 0:
  acumulador += numero
  numero = int(input("Ingrese otro número: "))

if numero == 0 and acumulador == 0:
  print("El número ingresado es 0")
else:
  print(f"El total acumulador es: {acumulador}")

#Ejercicio 5
from random import randint

aleatorio = randint(0, 9)
adivina = int(input("Adivina el número generado entre 0 y 9: "))
intentos = 0

while aleatorio != adivina:
  intentos += 1
  print("Incorrecto! Intenta de nuevo")
  adivina = int(input("Adivina el número generado: "))

print(f"Felicitaciones! Adivinaste el número ({adivina}), lo lograste despues de {intentos} intentos.")

#Ejercicio 6
for i in range(100, 0, -2):
  print(i)

#Ejercicio 7
numero = int(input("Ingrese un número entero mayor a 0:"))
acumulador = 0

if numero > 0:
  #Al no haber sido indicado si debía ser incluido o no el número ingresado en el acumulado, se ha elegido incluirlo. Para no incluirlo, solo debemos modificar el parámetro del loop.
  for i in range(numero + 1):
    acumulador += i

  print(f"La suma acumulada de los numeros comprendidos entre 0 y {numero}, es: {acumulador}")
else:
  print("El número ingresado no es mayor que 0")

#Ejercicio 8
limite_input, contador, pares, impares, negativos, positivos = 100, 1, 0, 0, 0, 0

while contador <= limite_input:
  numero = int(input("Ingrese un número entero: "))
  contador += 1
  if numero > 0:
    positivos += 1
    if numero % 2 == 0:
      pares += 1
    else:
      impares += 1
  elif numero < 0:
    negativos += 1
    if numero % 2 == 0:
      pares += 1
    else:
      impares += 1
  else:
    #Este es el caso del 0.
    pares += 1
  
print(f"Has ingresado {pares} números pares y {impares} números impares.")
print(f"También has ingresado {positivos} números positivos y {negativos} números negativos.")

#Ejercicio 9
limite_input, contador, acumulador = 100, 1, 0 

while contador <= limite_input:
  numero = int(input("Ingresa un número: "))
  contador += 1
  acumulador += numero

print(f"La media de los números ingresados es {acumulador / limite_input}")

#Ejercicio 10
numero = int(input("Ingresa un número para invertir sus dígitos: "))
numero = str(numero)
invertido = ""

for i in range(len(numero) - 1, -1 , -1):
  invertido += numero[i]

invertido = int(invertido)
print(f"El número ingresado, al ser invertido es: {invertido}")