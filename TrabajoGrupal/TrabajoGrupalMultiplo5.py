b = 0
print("Programa que muestra los multiplos de 5 del 0 a 100")
for i in range(0, 101):
    b = 0
    while b == 0:
        if i % 5 == 0:
            b = 1
            print(i)
        else:
            b = 1
