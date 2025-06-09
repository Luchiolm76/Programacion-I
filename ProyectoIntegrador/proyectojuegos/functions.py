
#metodo de ordenamiento por burbuja
def bubble_sort(juegos, key):
    n = len(juegos)
    for i in range(n):
        # Últimos i elementos ya están en su lugar
        for j in range(0, n - i - 1):
            if juegos[j][key] > juegos[j + 1][key]:
                temp = juegos[j]
                juegos[j] = juegos[j + 1]
                juegos[j + 1] = temp
    # Retornamos la lista ordenada
    return juegos

#ordenamiento quick sort
def quick_sort(juegos, key):  
    if len(juegos) <= 1:
        return juegos
    left = []
    middle = []
    right = []
    # Elegimos un pivote, en este caso el elemento del medio
    pivot = juegos[len(juegos) // 2][key]
    for x in juegos:
        if x[key] < pivot:
            left.append(x)
        elif x[key] > pivot:
            right.append(x)
        else:
            middle.append(x)
    return quick_sort(left, key) + middle + quick_sort(right, key)




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

# Búsqueda lineal para encontrar juegos por clave y valor
def busqueda_lineal(lista, clave, valor):
    resultados = []
    for item in lista:
        if item[clave] == valor:
            resultados.append(item)
    return resultados


