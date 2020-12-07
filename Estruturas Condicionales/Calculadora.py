n1 = 0; n2 = 0; r =0; O = 0;

print("Calculadora de operaciones básicas\n")
#Lectura de datos
n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
#Menú de opciones
print("Escoga una de las siguientes opciones")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
O = int(input())
#Seleccion de opciones
if O == 1:
    r = n1 + n2
    print("La respuesta de la suma es: ", r)
elif O == 2:
    r = n1 - n2
    print("La respuesta de la resta es: ", r)
elif O == 3:
    r = n1 * n2
    print("La respuesta de la multiplicación es: ", r)
elif O == 4:
    r = n1 / n2
    print("La respuesta de la división es: ", r)
elif (O > 4) ^ (O <= 0):
    print("Opción invalida")
