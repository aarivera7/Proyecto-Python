cont = 1; limite = 0; suma = 0;
        
#Pedir que se ingrese el limite de los numeros
limite = int(input("Ingrese la cantidad de numeros que quiere que se imprima: "))

#Iniciamos el ciclo repetitivo While
while cont <= limite:
    print(cont)
    suma = suma + cont
    cont = cont + 1
print("\nLa suma de los números es: ", suma)
