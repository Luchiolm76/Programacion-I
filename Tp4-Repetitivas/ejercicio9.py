cantidad = 5
media = 0

for i in range(cantidad):
    num = int(input("Ingrese 100 numeros enteros:"))
    media = media + num

media = media / cantidad

print(f"La media es:",media)
