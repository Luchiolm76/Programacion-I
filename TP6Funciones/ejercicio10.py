def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
a = float(input("Primer número: "))
b = float(input("Segundo número: "))
c = float(input("Tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")
