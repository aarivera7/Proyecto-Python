# Declaracion e inializacion de variables
dE = 0; mE = 0; aE  = 0; dEa = 0; mEa = 0; aEa = 0; dS = 0; mS = 0; aS = 0;
#Lectura de datos
print("Programa para saber tu edad en días, meses y años.")
dE = int(input("Ingrese el dia de su nacimiento: "))
mE = int(input("Ingrese el mes de su nacimiento: "))
aE = int(input("Ingrese el año de su nacimiento: "))
dEa = int(input("Ingrese que día del mes estas actuamente (en números): "))
mEa = int(input("Ingrese en que mes estas actualmente (en números): "))
aEa = int(input("Ingrese el año actual: "))
#Proceso
aS = aEa - aE;
if (mE <= mEa)&(mE > 1):
    if (dE > dEa)&(mE == mEa):
        aS = aS -1;
        mS = (mEa+12)-mE;
        if mS > 12:
            mS = mS - 12;
    else:
        mS = (mEa+12)-mE;
        if mS > 12:
            mS = mS - 12;
else:
    if(mEa == 12)&(mE == 1):
        aS = aS -1;
        mS = 1;
    else:
        aS = aS - 1;
        mS = (mEa+12)-mE;
        if mS > 12:
            mS = mS - 12;
    if(mE == 1)&(mEa ==1):
        aS = aS + 1;
if (dE <= dEa):
    dS = dEa - dE;
    if (mS == 12):
        mS = mS - 12;
else:
    mS = mS - 1
    dS = (dEa + 30) - dE
#Salida de Datos
print("Su edad actual es: ", aS," años, ", mS, " meses y ", dS, " días")
