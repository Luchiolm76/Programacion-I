def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci_hasta(n):
    for i in range(n + 1):
        print(f"F({i}) = {fibonacci(i)}")

# Ejemplo:
mostrar_fibonacci_hasta(7)

