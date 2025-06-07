def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# Ejemplo:
print(es_palindromo("neuquen"))  # True
print(es_palindromo("python"))   # False
