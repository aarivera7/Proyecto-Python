#Declaración de variables
Tipo = 1; Cant = 0; Desc1 = 0.3; Desc2 = 0.2; Desc3 = 0.1; Costo = 0; 
DescTotal = 0; Total = 0; Name = "";Desc = 0;d = 0;
        
#Lectura de Datos
Name =input("Ingrese el nombre del cliente:\n")
Tipo = int(input("Ingrese el tipo de cliente que es:\n 1. Si es profesor\n"+
                    " 2. Si es estudiante\n 3. Otro\n"))
Costo = float(input("Ingrese el costo del libro:\n"))
Cant = int(input("Ingrese la cantidad de libros:\n"))
        
#Proceso
if Tipo == 1:
    Costo = Costo * Cant;
    Total = Costo - (Costo * Desc1);
    DescTotal = 30;
    Desc = (Costo * Desc1);
    d = 0.30;
if Tipo == 2:
    Costo = Costo * Cant;
    Total = Costo - (Costo * Desc2);
    DescTotal = 20;
    Desc = (Costo * Desc2);
    d = 0.20;
if Tipo == 3:
    Costo = Costo * Cant;
    Total = Costo - (Costo * Desc3);
    DescTotal = 10;
    Desc = (Costo * Desc3);
    d = 0.10;
if (Cant > 5)&(Cant <= 10):
    Total = Costo - (Costo *(0.04 + d));
    DescTotal = DescTotal + 4;
    Desc = Desc + (Costo *0.04);
if Cant > 10:
    Total = Costo - (Costo *(0.08 + d));
    DescTotal = DescTotal + 8;
    Desc = Desc + (Costo *0.08);
print("El nombre del cliente es: "+Name+ "\nEl subtotal es: %", Costo, 
    "$\nEl descuento total es: $", Desc,"  ",DescTotal, "% \nEl total a pagar es: $",
      Total);
