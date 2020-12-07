h24 = 0; m24 = 0; h12 = 0; m12 =0;periodo = "a.m.";

print("Programa para convertir las horas en formato de 24 horas a 12 horas\n")

#Ingresar los datos de entrada
h24 = float(input("Ingrese la hora en formato 24 a transformar: "))
m24 = float(input("Ingrese los minutos a transformar: "))

if (h24 < 25) & (h24 >= 0):
    if ((h24 > 0) & (h24 < 24) & (m24 >= 0) & (m24 <=60)):
        if m24 == 60:
            h24 = h24 + 1
            m24 = 0
        else:
            m12 = m24
            
        if h24 >= 12:
            if h24 == 12:
                h12 = h24
                periodo = "p.m."

            else:
                h12 = h24 -12
                periodo = "p.m."
        else:
            h12 = h24

        print("El tiempo de ", h24," hora y ", m24," minutos, en formato de 24 horas")
        print("Equivale a " , h12," hora y ", m12," minutos ", periodo)

    else:
        if h24 == 24:
            h12 = 12
            h24 = 0
            if m24 == 60:
                h12 = h12 + 1
                h12 = h12 - 12
                h24 = h24 + 1
                m24 = 0
        else:
            h12 = 12
            if m24 == 60:
                h12 = h12 + 1
                h12 = h12 - 12
                h24 = 1
                m24 = 0
            else:
                m12 = m24
                
        print("El tiempo de ", h24," hora y ", m24," minutos, en formato de 24 horas")
        print("Equivale a " , h12," hora y ", m12," minutos ", periodo)

else:            
    print("Error el valor ingresado no esta en formato de 24 horas")
