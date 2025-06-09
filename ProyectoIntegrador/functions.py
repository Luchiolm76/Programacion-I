# functions.py
# modules/functions.py
"""juegos = [
    {"titulo": "Celeste", "anio": 2018, "puntaje": 92},
    {"titulo": "Hades", "anio": 2018, "puntaje": 93},
    {"titulo": "The Witcher 3", "anio": 2015, "puntaje": 96},
]"""

from listajuegos import juegos as juegos


def bubble_sort(juegos, key):
    n = len(juegos) - 1
    for i in range(0, n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i):
            if juegos[j][key] > juegos[j + 1][key]:
                temp = juegos[j]
                juegos[j] = juegos[j + 1]
                juegos[j + 1] = temp
    # Retornamos la lista ordenada
    return juegos

def busqueda_binaria(lista, clave, valor):
    inicio = 0
    fin = len(lista) - 1
    resultados = []
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio][clave] == valor:
            resultados.append(lista[medio])
            # Buscamos hacia la izquierda
            izquierda = medio - 1
            while izquierda >= inicio and lista[izquierda][clave] == valor:
                resultados.append(lista[izquierda])
                izquierda -= 1
            # Buscamos hacia la derecha
            derecha = medio + 1
            while derecha <= fin and lista[derecha][clave] == valor:
                resultados.append(lista[derecha])
                derecha += 1
            break  # Ya encontramos todos los resultados
        elif lista[medio][clave] < valor:
            inicio = medio + 1
        else:
            fin = medio - 1
    return resultados

# Ordenar la lista antes de buscar
juegos_ordenados = bubble_sort(juegos, 'anio') # Ordenamos por puntaje
print(busqueda_binaria(juegos_ordenados, 'anio', 2018))  # Debería retornar los juegos de 2018


def busqueda_lineal(lista, clave, valor):
    resultados = []
    for item in lista:
        if item[clave] == valor:
            resultados.append(item)
    return resultados


print("Búsqueda lineal de juegos de 2018:")
# Ordenar la lista antes de buscar
print(busqueda_lineal(juegos, 'anio', 2018))  # Debería retornar los juegos de 2018


