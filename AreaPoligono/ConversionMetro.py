#Declaracion e Inializacion de variables
M = 0
Ck = 0.001
Cft = 3.2808
Cp = 39.3701
Cc = 100
O = 0
R = 0
print("Programa que permite convertir de metros a kilómetros, pies, pulgadas y centímetros.")
print("")

#Entrada, Proceso y Salida de Datos

O = int(input("""Elige una opción:
       1. Para pasar de metros a kilómetros.
       2. Para pasar de metros a pies.
       3. Para pasar de metros a pulgadas.
       4. Para pasar de metros a centímetros.
       """))
if O == 1:
    M = float(input("Ingrese el valor en metros que quiere convertir a kilómetros: "))
    R = M*Ck
    print("El resultado es: ",R,"km")
elif O == 2:
    M = float(input("Ingrese el valor en metros que quiere convertir a pies: "))
    R = M*Cft
    print("El resultado es: ",R,"ft")
elif O == 3:
    M = float(input("Ingrese el valor en metros que quiere convertir a pulgadas: "))
    R = M*Cp
    print("El resultado es: ",R," pulgadas")
elif O == 4:
    M = float(input("Ingrese el valor en metros que quiere convertir a centímetros: "))
    R = M*Cc
    print("El resultado es: ",R,"cm")
else:
    print("La opción que elegiste no existe")
