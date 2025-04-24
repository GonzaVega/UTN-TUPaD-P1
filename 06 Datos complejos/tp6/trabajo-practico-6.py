#Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

#Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

#Ejercicio 3
lista_frutas = [precios_frutas.keys()]

print(lista_frutas)

#Ejercicio 4
class Persona():
  def __init__(self, nombre, pais, edad):
    self.nombre = nombre
    self.pais = pais
    self.edad = edad

  def saludar(self):
    return print(f"¡Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")

nombre_usuario = input("Ingrese su nombre: ")
pais_usuario = input("Ingrese su país: ")
edad_usuario = input("Ingrese su edad: ")
persona1 = Persona(nombre_usuario, pais_usuario, edad_usuario)

persona1.saludar()

#Ejercicio 5
from math import pi

class Circulo():
  def __init__(self, radio):
    self.radio = radio

  def calcular_area(self):
    area = pi * (self.radio ** 2)
    return print(f"El área de su círculo es: {round(area, 2)}")
  
  def calcular_perimetro(self):
    perimetro = (self.radio * 2) * pi 
    return print(f"El área de su círculo es: {round(perimetro, 2)}")

radio_usuario = float(input("Ingrese el radio de su círculo, obtendrá su área y su perímetro: "))

circulo1 = Circulo(radio_usuario)

circulo1.calcular_area()
circulo1.calcular_perimetro()

#Ejercicio 7
class Cola():
  #Se inicializa la clase con la capacidad de atención que tiene el banco.
  def __init__(self, capacidad):
    self.clientes = []
    self.capacidad_de_atencion = capacidad - 1

  def mostrar_clientes(self):
    for i in self.clientes:
      print (f"Cliente pendiente: {i}")
  
  def agregar_cliente(self, elemento):
    self.clientes.insert(0, elemento)
  
  def atender_cliente(self):
    print(f"Es el turno del cliente: {self.clientes[-1]}")
    self.clientes.pop()

  def mostrar_siguiente(self):
    return print(f"El próximo cliente es: {self.clientes[-1]}")
  
clientes_banco = Cola(3)

while len(clientes_banco.clientes) <= clientes_banco.capacidad_de_atencion:
  clientes_banco.agregar_cliente(input("Ingrese el nombre del cliente a atender: "))

clientes_banco.mostrar_clientes()
clientes_banco.atender_cliente() 
clientes_banco.mostrar_siguiente()
clientes_banco.mostrar_clientes()

# Ejercicio 8

class Nodo:
  def __init__(self, numero):
    self.numero = numero
    self.siguiente = None
    self.anterior = None

class Lista:
  def __init__(self):
    self.inicio = None
    self.final = None
  
  def agregar_item(self, item):
    item = Nodo(item)
    if self.inicio == None:
      self.inicio = item
      self.final = item
    else:
      item.anterior = self.final
      self.final.siguiente = item
      self.final = item

  def mostrar(self):
    sentido = input("Ingrese 'A' para recorrer de inicio a fin, o 'I' para sentido inverso: ")
    sentido = sentido.lower()
    if sentido == "a":
      elemento = self.inicio
      while elemento:
        print(elemento.numero, end= "->")
        elemento = elemento.siguiente
      print("None")

# Ejercicio 9      
    elif sentido == "i":
      elemento = self.final
      while elemento:
        print(elemento.numero, end= "->")
        elemento = elemento.anterior
      print("None")
    else:
      print("La opción ingresada es incorrecta.")

mi_lista = Lista()

mi_lista.agregar_item(1)
mi_lista.agregar_item(2)
mi_lista.agregar_item(3)
mi_lista.mostrar()
