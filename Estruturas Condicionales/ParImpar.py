#El número a verificar si es par
num = 0; tipo = ""
        
print("Programa para verificar si un número es par o impar\n")
num = float(input("Ingrese el número a verificar:\n"))  #Ingresa el nuemro  
        
if num % 2 == 0:
    tipo = "par"
else:
    tipo = "impar"
print("\nEl número ", num, " es "+ tipo)
