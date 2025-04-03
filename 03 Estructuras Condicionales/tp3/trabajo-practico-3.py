#Ejercicio 1
edad = int(input("Ingrese su edad: "))

if edad >= 18:
  print("Es mayor de edad")

#Ejercicio 2
nota = float(input("Ingrese su nota: "))

if nota >= 6:
  print("Aprobado")
else:
  print("Desaprobado")

#Ejercicio 3
numero = float(input("Ingrese un número: "))

if numero % 2 == 0:
  print("Ha ingresado un número par.")
else:
  print("Por favor, ingrese un número par.")

#Ejercicio 4
edad = int(input("Ingrese su edad: "))

if edad >= 0 and edad < 12:
  print("Niño/a")
elif edad >= 12 and edad < 18:
  print("Adolescente")
elif edad >= 18 and edad < 30:
  print("Adulto/a joven")
elif edad >= 30:
  print("Adulto/a")
else:
  print("Ingrese un valor de edad positivo.")

#Ejercicio 5
password = input("Ingrese una contraseña: ")

if len(password) >= 8 and len(password) <= 14:
  print("Ha ingresado una contraseña correcta.")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#Ejercicio 6
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda, mediana, media = mode(numeros_aleatorios), median(numeros_aleatorios), mean(numeros_aleatorios) 

if moda == mediana == media:
  print("Sin sesgo")
elif media > mediana and mediana > moda:
  print("Sesgo Positivo")
elif media < mediana and mediana < moda:
  print("Sesgo Negativo")
else:
  print("No se puede determinar sesgo.")

print(f"Moda: {moda}, Mediana: {mediana}, Media: {media}")

#Ejercicio 7
cadena = input("Ingrese una palabra o frase: ").lower()

vocales = ["a", "e", "i", "o", "u"]

if cadena[-1] in vocales:
  print(cadena + "!")
else:
  print(cadena)

#Ejercicio 8
nombre = input("Ingrese su nombre: ")
numero = int(input("Ingrese 1 para nombre en mayúscula, 2 para minúsculas y 3 para estilo título: "))

if numero == 1:
  print(nombre.upper())
elif numero == 2:
  print(nombre.lower())
elif numero == 3:
  print(nombre.title())
else:
  print("Ingrese un número válido.")

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud de un terremoto: "))

if magnitud >= 0 and magnitud < 3:
  print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
  print("Leve")
elif magnitud >= 4 and magnitud < 5: 
  print("Moderado")
elif magnitud >= 5 and magnitud < 6: 
  print("Fuerte")
elif magnitud >= 6 and magnitud < 7: 
  print("Muy Fuerte")
elif magnitud >= 7: 
  print("Extremo")
else: 
  print("Magnitud no válida") 

#Ejercicio 10
hemisferio = input("Ingrese en que hemisferio se encuentra (N/S): ").lower()
dia = int(input("Ingrese el día del mes: "))
mes = int(input("Ingrese el mes del año: "))

#Se utilizaran estructuras condicionales anidadas para tener control de la validez de los datos ingresados.
if hemisferio == "n":
  # Se considerarán aquí todos los casos para el hemisferio norte.
  if mes > 0 and mes < 3 or (mes == 12 and dia >= 21 and dia <= 31) or (mes == 3 and dia <= 20):
    print("Invierno")
  elif mes > 3 and mes < 6 or (mes == 3 and dia >= 21 and dia <= 31) or (mes == 6 and dia <= 20):
    print("Primavera")
  elif mes > 6 and mes < 9 or (mes == 6 and dia >= 21 and dia <= 30) or (mes == 9 and dia <= 20):
    print("Verano")
  elif mes > 9 and mes < 12 or (mes == 9 and dia >= 21 and dia <= 30) or (mes == 12 and dia <= 20):
    print("Otoño")
  else:
    print("Día o mes no válidos.")
elif hemisferio == "s":
  # Se considerarán aquí todos los casos para el hemisferio sur.
  if mes > 0 and mes < 3 or (mes == 12 and dia >= 21 and dia <= 31) or (mes == 3 and dia <= 20):
    print("Verano")
  elif mes > 3 and mes < 6 or (mes == 3 and dia >= 21 and dia <= 31) or (mes == 6 and dia <= 20):
    print("Otoño")
  elif mes > 6 and mes < 9 or (mes == 6 and dia >= 21 and dia <= 30) or (mes == 9 and dia <= 20):
    print("Invierno")
  elif mes > 9 and mes < 12 or (mes == 9 and dia >= 21 and dia <= 30) or (mes == 12 and dia <= 20):
    print("Primavera")
  else:
    print("Día o mes no válidos.")
else:
  print("Hemisferio ingresado no válido.")