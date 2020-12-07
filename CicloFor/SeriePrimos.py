num = 0; den = 1; n = 0; divisor = 0; i2 = 1; v = 0; suma = 0;
print("Programa que muestra la serie 1/2 + -2/3 + 3/5 + -4/7 + 5/11")
n = int(input("Ingrese el limite de la serie\n"))
for i in range(1,(n+1)):
    num = i
    v = 0
    while v == 0:
        den = den + 1
        i2=1
        for i2 in range(i2,(den+1)):
            if den % i2 == 0:
                divisor = divisor + 1
        if divisor == 2:
            v = 1
        divisor = 0
    if i % 2 == 0:
        print(i, ". ", -num, " / ", den)
    else:
        print(i, ". ", num, " / ", den)
    suma = suma + ((-1)**(i+1))*(num/den)
print("Suma total de los terminos: ", suma)
