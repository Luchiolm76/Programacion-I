def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

# Ejemplo:
print(contar_bloques(4))  # 10
