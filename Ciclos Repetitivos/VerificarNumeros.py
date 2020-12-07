#Decalarar e inicializar variables
cont = 1; n = 1; num = 0; sumPar = 0; sumImpar = 0; sumNeg = 0; sumPos = 0;
        
#Ingresar los datos de entrada: límite
n = int(input("Ingrese el límite de números a verificar: "))
        
#Crear el ciclo para verificar los numeros
while cont <= n:
    num = int(input("\nIngrese el número a verificar: "))
            
    if (num % 2 == 0):  #Verificar si es par o impar
        sumPar = sumPar + num;    #Suma los pares
    else:
        sumImpar = sumImpar + num;    #Suma los impares
    if num > 0:  #Verificar si es positivo o negativo
        sumPos = sumPos + num;    #Suma los positivos
    else:
        sumNeg = sumNeg + num;    #Suma los negativos

    cont = cont + 1;
    print("La suma de los pares: ", sumPar)
    print("La suma de los impares: ", sumImpar)
    print("La suma de los positivos: ", sumPos)
    print("La suma de los negativos: ", sumNeg)

print("\nSumas totales\n")
print("La suma de los pares: ", sumPar)
print("La suma de los impares: ", sumImpar)
print("La suma de los positivos: ", sumPos)
print("La suma de los negativos: ", sumNeg)
