import random
numero_random = random.randint(0,9)

intentos = 1
while True:
    numero = int(input("Adivina el numero chaval del 0 al 9:"))
    if numero == numero_random:
        break
    else:
        intentos += 1

print(f"Adivinaste e hiciste {intentos} intentos")