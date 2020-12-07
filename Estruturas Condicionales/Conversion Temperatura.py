gC = 0
gF = 0
gK = 0

print("Programa para convertir de grados Celsius a grados Kelvin y Fahrenheit\n")
gC = float(input("Ingrese el valor de gC\n"))

#Condicion para conversion de grados de temperatura
if gC > 0:
    gF = (gC * 9 / 5) + 32
    gK = gC + 273.15
    print("La equivalencia en grados F es ", gF)
print("La equivalencia en grados K es ", gK)

