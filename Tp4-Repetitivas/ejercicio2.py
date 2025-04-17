num = int(input("Ingrese un numero entero:"))

num = abs(num)

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        num = num // 10
        count += 1

print(f"El numero tiene:{count} digitos")
