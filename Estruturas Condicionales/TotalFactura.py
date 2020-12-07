#Declaracion e inalizacion de variables
        
subtotal = 0; total = 0; descuento = 0; limite1 = 200; limite2 =500; desc = 0;
        
print("Programa para calcular el valor total de una factura con descuento")
        
#Ingresar datos de entrada
subtotal = float(input("Ingrese el subtotal de la compra: \n"))
        
if (subtotal >= limite1) & (subtotal < limite2):
    descuento = 0.10;
else:
    if subtotal >= limite2:
        descuento = 0.15
total = subtotal - (subtotal*descuento)
desc = subtotal*descuento
if subtotal < limite1:
    print("No hay descuento por su compra por ser menor a 200 dolares")
    
#Salida de datos
print("El total de la factura es $", total, " con un descuento de $", desc,
      " del ",descuento*100, "%")
