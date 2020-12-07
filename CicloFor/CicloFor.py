n = 0; a = 0; b = 1; c = 0; suma = 0;
print("Programa que muestra la serie de fibonacci")
n = int(input("Ingrese el limite de la suceción de Fibinacci: "))
print()
for i in range(1,(n+1)):
    print(i, ". ", a, "")
    suma = suma + a
    c = a + b
    a = b
    b = c
print()
print("La suma de los terminos de la suceción es: ", suma)
