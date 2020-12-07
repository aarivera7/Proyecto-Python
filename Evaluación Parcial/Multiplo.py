#Declaración de variables
n = 0
        
#Lectura de Datos
n = float(input("Ingrese un número:\n"))
        
#Proceso
if n < 100:
    if n % 4 == 0:
        n = n / 2;
        print("Su número es: ",n)
    else:
        if n % 5 == 0:
            n = n ** 2;
            print("Su número es: ",n)
        else:
            if n % 6 == 0:
                print("Su número es: ",n)
else:
    print("Error: Su número es mayor a 100")
