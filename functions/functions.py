# Funcion de busqeuda por nombre
def buscar_por_nombre(lista, nombre_buscado):
    for juego in lista:
        if juego["nombre"].lower() == nombre_buscado.lower():
            return juego
    return None
# Llamas a la funcion para ver el resultado
nombre_a_buscar = input("🔍 Ingrese el nombre del videojuego que quiera buscar: ")

resultado = buscar_por_nombre(videojuegos, nombre_a_buscar)

if resultado:
    print("✅ Videojuego encontrado:")
    print(f"Nombre: {resultado['nombre']}")
    print(f"Año: {resultado['año']}")
    print(f"Género: {resultado['género']}")
    print(f"Puntuación: {resultado['puntuación']}")
else:
    print("❌ No se encontró el videojuego.")


# Funcion por seleccion seleccion sort
def ordenar_por_año(lista):
    n = len(lista)
    for i in range(n - 1):
        max_idx = i
        for j in range(i + 1, n):
            if lista[j]["año"] > lista[max_idx]["año"]:
                max_idx = j
        # Intercambiamos el más nuevo con el que está en la posición i
        aux = lista[i]
        lista[i] = lista[max_idx]
        lista[max_idx] = aux

# Llamar a la funcion
# Ordeno por año de lanzamiento
ordenar_por_año(videojuegos)

# Mostramos los videojuegos ordenados por año
print("\n📅 Videojuegos ordenados por año (más reciente a más antiguo):")
for juego in videojuegos:
    print(f"{juego['nombre']} - Año: {juego['año']}")

# Funcion de insercion sort
def ordenar_por_nombre(lista):
    n = len(lista)
    for i in range(1, n):
        actual = lista[i]
        j = i - 1
        while j >= 0 and lista[j]["nombre"].lower() > actual["nombre"].lower():
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = actual

#LLamar a la funcion
# Ordenamos por nombre alfabéticamente
ordenar_por_nombre(videojuegos)

print("\n🔠 Videojuegos ordenados alfabéticamente por nombre:")
for juego in videojuegos:
    print(f"{juego['nombre']}")
