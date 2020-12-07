n = 0; suma = 0; i = 0; b = 0;
while b == 0:
    n = int(input("Ingrese un numero para la serie: "))
    suma += n
    i+=1
    if suma > 10000:
        b = 1
    else:
        if suma <= 10000:
            print("La suma de numeros introducidos hasta el momento es de: " 
                    , suma, " de 10000 posibles.")
    
print("Ha introducido un total de: ", i, " números.")
print("La suma total de la serie es: ", suma)
print("La media de la serie es:", suma / i)
