#Ejercicio 1
def imprimir_hola_mundo():
  return print("Hola Mundo!")

imprimir_hola_mundo()

#Ejercicio 2
def saludar_usuario(nombre):
  return print(f"Hola {nombre}!")

usuario = input("Ingrese su nombre: ")
saludar_usuario(usuario)

#Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
  return print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

nombre_usuario = input("Ingrese su nombre: ")
apellido_usuario = input("Ingrese su apellido: ")
edad_usuario = input("Ingrese su edad: ")
residencia_usuario = input("Ingrese su residencia: ")

informacion_personal(nombre_usuario, apellido_usuario, edad_usuario, residencia_usuario)

#Ejercicio 4
from helpers import valida_numero
from math import pi

def calcular_area_circulo(radio):
  valida_numero(radio, "área")
  area = pi * (radio **2)
  return print(f"El área de su círculo es {round(area, 2)}")
  
def calcular_perimetro_circulo(radio):
  valida_numero(radio, "perímetro")
  perimetro = (radio * 2) * pi 
  return print(f"El perímetro de su círculo es {round(perimetro, 2)}")
  
radio_usuario = float(input("Ingrese el radio de su círculo: "))

calcular_area_circulo(radio_usuario)
calcular_perimetro_circulo(radio_usuario)

#Ejercicio 5
def segundos_a_horas(segundos):
  valida_numero(segundos, "calcular horas")
  horas = (segundos / 60 ) / 60
  return print(f"El equivalente en horas de los segundos ingresados es: {round(horas, 2)}")

segundos_usuario = int(input("Ingrese segundos para averiguar a cuantas horas equivale: "))

segundos_a_horas(segundos_usuario)

#Ejercicio 6
def tabla_multiplicar(numero):
  valida_numero(numero, "tabla de multiplicar")
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero_usuario = int(input("Ingrese un número para ver su tabla de mulplicar: "))

tabla_multiplicar(numero_usuario)

#Ejercicio 7
def operaciones_basicas(numA, numB):
  valida_numero(numA, "el primer número")
  valida_numero(numB, "el segundo número")
  suma = numA + numB
  resta = numA - numB
  multiplicacion = numA * numB
  division = numA / numB
  return print(f"El resultado de sumar los dos números ingresados es: {suma}.\nEl de restar el primero al segundo es: {resta}.\nSi los multiplicamos, es: {multiplicacion}.\nY si dividimos el primero por el segundo, es: {division}.")

primer_numero = float(input("Ingrese el primer número: "))
segundo_numero   = float(input("Ingrese el segundo número: "))

operaciones_basicas(primer_numero, segundo_numero)

#Ejercicio 8
def calcular_imc(peso, altura):
  valida_numero(peso, "el peso")
  valida_numero(altura, "la altura")
  imc = peso / (altura * 2)
  return print(f"Su IMC es de: {round(imc, 2)}")

peso_usuario = float(input("Ingrese su peso en kilos: "))
altura_usuario = float(input("Ingrese su altura en metros: "))

calcular_imc(peso_usuario, altura_usuario)

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
  valida_numero(celsius, "la temperatura")
  fahrenheit = (celsius * (9/5)) + 32
  return print(f"{celsius}° celsius equivalen a {round(fahrenheit, 1)}° fahrenheit")

grados_usuario = float(input("Ingrese su temperatura en grados celsius: "))

celsius_a_fahrenheit(grados_usuario)

#Ejercicio 10
def calcular_promedio(nota1, nota2, nota3):
  valida_numero(nota1, "la primera nota")
  valida_numero(nota2, "la segunda nota")
  valida_numero(nota3, "la tercera nota")
  promedio = (nota1 + nota2 + nota3) / 3
  return print(f"El promedio de las notas ingresadas es: {round(promedio, 2)}")

primera_nota = float(input("Ingrese la primera nota: "))
segunda_nota = float(input("Ingrese la segunda nota: "))
tercera_nota = float(input("Ingrese la tercera nota: "))

calcular_promedio(primera_nota, segunda_nota, tercera_nota)  