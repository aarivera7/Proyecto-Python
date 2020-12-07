#Declaracion de variables
n1 = 0; n2 = 0; n3 =0;
        
#Ingreso de datos de entrada
print("Programa para averiguar cuál es el número mayor de tres números\n")
        
n1 = float(input("Ingrese el primer número:\n"))
n2 = float(input("Ingrese el segundo número:\n"))
n3 = float(input("Ingrese el tercero número:\n"))
        
#Proceso
        
if (n1 > n2) & (n1 > n3):
    print("El primer número: ", n1, " es el mayor")
if (n2 > n1) & (n2 > n3):
    print("El segundo número: ", n2, " es el mayor")
if (n3 > n1) & (n3 > n2):
    print("El tercer número: ", n3, " es el mayor")
else:
    print("Los valores que ingresaste son iguales")
