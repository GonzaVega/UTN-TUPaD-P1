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
  return print(f"El área de su círculo es {area}")
  
def calcular_perimetro_circulo(radio):
  valida_numero(radio, "perímetro")
  perimetro = (radio * 2) * pi 
  return print(f"El perímetro de su círculo es {perimetro}")
  
radio_usuario = float(input("Ingrese el radio de su círculo: "))

calcular_area_circulo(radio_usuario)
calcular_perimetro_circulo(radio_usuario)

#Ejercicio 5
def segundos_a_horas(segundos):
  valida_numero(segundos, "calcular horas")
  if not valida_numero:  
    horas = (segundos / 60 ) / 60
    return print(f"El equivalente en horas de los segundos ingresados es: {horas}")

segundos_usuario = input("Ingrese segundos para averiguar a cuantas horas equivale: ")

segundos_a_horas(segundos_usuario)

#Ejercicio 6
def tabla_multiplicar(numero):
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero_usuario = int(input("Ingrese un número para ver su tabla de mulplicar: "))

tabla_multiplicar(numero_usuario)

#Ejercicio 7

