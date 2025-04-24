# Ejercicio 1
lista = list(range(4, 101, 4))
print(lista)

# Ejercicio 2
lista = [1, 2, 3, 4, 5]
print(lista[-2])

#Ejercicio 3
lista = []
lista.append("Perro")
lista.append("Casa")
lista.append("Auto")

print(lista)

# Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"

print(animales)

# Ejercicio 5

# El programa dado consiste en una lista, a la cual luego se le aplica el metodo remove(), que quita elementos de la misma, y se le pasa como parametro a esa funcion, el metodo max() que busca el valor mas alto dentro de la lista. 
# Como resultado en la impresión por pantalla, obtendremos la lista, menos el valor maximo original que era numeros[3], equivalente a 22.

#Ejercicio 6
lista = list(range(10, 31, 5))

print(lista[0], lista[-1])

# Ejercicio 7
autos = ["sedan", "polo", "suran", "gol"]
autos[1], autos[2] = "rojo", "SUV"

print(autos)

# Ejercicio 8
dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)

# Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

# Ejercicio 10
lista_anidada = []
lista_anidada.extend([15, True])
lista_anidada.append([25.5, 57.9, 30.6])
lista_anidada.append(False)

print(lista_anidada)


