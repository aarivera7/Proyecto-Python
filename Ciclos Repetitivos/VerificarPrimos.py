#Declaración e inialización de variables
n = 0; num = 0; cont = 1; divisor = 0; i = 1;
        
#Entrada de datos
n = int(input("Ingrese el límite de números a verificar: "))
        
#Crear el ciclo para verificar los numeros
while cont <= n:
    num = int(input("Ingrese el valor para verificar si es prímo: "))
    while i <= num:
        if num % i == 0:
            divisor = divisor + 1
        i = i + 1
    if divisor == 2:
        print("El numero : ", num, " es primo")
        print("------------")
    else:
        print("El numero : ", num, " no es primo")
        print("------------")

    #Termina de verificar y reinicia contadores
    cont = cont + 1
    divisor = 0
    i = 1
