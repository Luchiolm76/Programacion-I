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


def quick_sort(juegos, key):
    if len(juegos) <= 1:
        return juegos
    left = []
    middle = []
    right = []
    # Elegimos un pivote, en este casoo el elemento del medio
    pivot = juegos[len(juegos) // 2][key]
    for x in juegos:
        if x[key] < pivot:
            left.append(x)
        elif x[key] > pivot:
            right.append(x)
        else:
            middle.append(x)
    return quick_sort(left, key) + middle + quick_sort(right, key)


# Ordenamos la lista de juegoss por puntaje usando quicksort
print("Lista de juegos ordenada por puntaje mediante quicksort:")
juegos_ordenadosQS = quick_sort(juegos, 'anio')  # Ordenamos por año
print(juegos_ordenadosQS)  # Imprimimos la lista ordenada por año

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
print("Lista de juegos ordenada por año mediante bubble sort:")
juegos_ordenados = bubble_sort(juegos, 'anio') # Ordenamos por puntaje
print(juegos_ordenados)  # Imprimimos la lista ordenada por año
#print(busqueda_binaria(juegos_ordenados, 'anio', 2018))  # Debería retornar los juegos de 2018


def busqueda_lineal(lista, clave, valor):
    resultados = []
    for item in lista:
        if item[clave] == valor:
            resultados.append(item)
    return resultados




