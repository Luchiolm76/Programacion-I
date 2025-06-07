def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# Ejemplo:
print(potencia(2, 4))  # 2^4 = 16

