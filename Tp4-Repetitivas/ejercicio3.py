num1 = int(input("Ingrese un numero entero:"))
num2 = int(input("Ingrese un numero entero:"))

inicio = min(num1, num2)+1
fin = max(num1,num2)

suma = 0

for i in range(inicio, fin):
    suma += i

print(f"La suma es: {suma}")