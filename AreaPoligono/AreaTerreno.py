#Declaración e inializacion de variables

A = 0; B = 0; C = 0; D = 0; at = 0; ar = 0; area = 0;

print("***Programa que permite el cálculo de un terreno***")
print("")

#Lectura de Datos

A = float(input("Ingrese el lado A del terreno: "))
B = float(input("Ingrese el lado B del terreno: "))
C = float(input("Ingrese el lado C del terreno: "))

#Proceso
D = A - C
at = (B * D) / 2
ar = B * C
area = at + ar

#Salida

print("El área del terreno es: ", area)
