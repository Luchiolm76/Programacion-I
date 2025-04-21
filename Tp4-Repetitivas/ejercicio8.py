pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(100):
    num = int(input("Ingrese 100 numeros enteros: "))
    if num % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if num > 0:
        positivos = positivos + 1
    else:
        negativos = negativos + 1
print(f"Cantidad de numeros pares:",pares)
print(f"Cantidad de numeros impares:",impares)
print(f"Cantidad de numeros positivos:",positivos)
print(f"Cantidad de numeros negativos:",negativos)