def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Para evitar cadena vacía en n = 0
def convertir_a_binario(n):
    if n == 0:
        return "0"
    return decimal_a_binario(n)

# Ejemplo:
print(convertir_a_binario(10))  # "1010"
