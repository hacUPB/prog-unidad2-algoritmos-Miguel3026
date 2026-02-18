## Punto 3 actividad 1:
# Programa para convertir un número decimal a binario

decimal = int(input("Ingrese un número decimal: "))

if decimal == 0:
    print("El número en binario es: 0")
else:
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        binario = str(residuo) + binario
        decimal = decimal // 2

    print("El número en binario es:", binario)
