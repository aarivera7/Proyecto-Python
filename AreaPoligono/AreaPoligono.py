lc = 0
at = 0
ar = 0
A = 0
B = 0
D = 0
ats = 0
area = 0
print("***Programa que permite el cálculo de un poligono compuesto. ***")
print("")

#Lectura de datos

lc = float(input("Ingrese el lado del cuadrado: "))
at = float(input("Ingrese la altura del triángulo: "))
ar = float(input("Ingrese la altura del rectángulo: "))

#Proceso

A = lc ** 2
B = (lc * at) / 2
ats = B * 3
D = lc * ar
area = A + ats + D

print("El área del poligono compuesto es:", area, ", compuesto por un cuadrado de lado\n " 
        , lc, ", un rectángulo de altura ", ar, " y una altura de triángulo ", at)
