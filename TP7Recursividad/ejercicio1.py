def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar factoriales entre 1 y un número dado por el usuario
def factoriales_hasta(n):
    for i in range(1, n + 1):
        print(f"{i}! = {factorial(i)}")

# Ejemplo:
factoriales_hasta(5)
