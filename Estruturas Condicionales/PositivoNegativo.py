#Declaracion e inializacion de variables
n = 0;
print("Programa que permite saber si un número es positivo o negativo\n")
n = float(input("Ingrese un numero:\n"))

#Proceso
if n > 0:
    print("El número: ", n, " es positivo.")
else:
    if n < 0:
        print("El número: ", n, " es negativo.")
    else:
        if n == 0:
            print("El número: ", n, " no es ni positivo, ni negativo.")
        else:
            print("El valor que digitaste no es valido")
