from functions import bubble_sort, quick_sort, busqueda_binaria, busqueda_lineal
from listajuegos import juegos




def menu():

    juegos_ordenados = juegos[:]
    
    print("Bienvenido al programa de juegos")
    print("1. Mostrar lista de juegos")
    print("2. Hacer ordenamiento de juegos por burbuja")
    print("3. Hacer ordenamiento de juegos rapido")
    print("4. Buscar un juego con busqueda binaria") 
    print("5. Buscar un juego con busqueda lineal") 
    print("6. Salir") 
    
    
    while True:
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            for juego in juegos_ordenados:
                print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
        elif opcion == '2':
            key = input("¿Por qué clave desea ordenar? titulo/anio/puntaje: ")
            juegos_ordenados = bubble_sort(juegos_ordenados, key)
            print("Lista ordenada por burbuja.")
            for juego in juegos_ordenados:
                print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
        elif opcion == '3':
            key = input("¿Por qué clave desea ordenar? titulo/anio/puntaje: ")
            juegos_ordenados = quick_sort(juegos_ordenados, key)
            print("Lista ordenada por quick sort.")
            for juego in juegos_ordenados:
                print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
        elif opcion == '4':
            clave = input("Ingrese la clave por la que desea buscar (titulo, anio, puntaje): ")
            valor = input(f"Ingrese el valor de {clave} que desea buscar: ")
            if clave in ['titulo', 'anio', 'puntaje']:
                if clave == 'anio':
                    valor = int(valor)
                    juegos_ordenados = bubble_sort(juegos_ordenados, 'anio')  # Aseguramos que la lista esté ordenada por 'anio'
                elif clave == 'puntaje':
                    valor = int(valor)
                    juegos_ordenados = bubble_sort(juegos_ordenados, 'puntaje')  # Aseguramos que la lista esté ordenada por 'puntaje'
                elif clave == 'titulo':
                    juegos_ordenados = bubble_sort(juegos_ordenados, 'titulo')
                resultados = busqueda_binaria(juegos_ordenados, clave, valor)
                print(f"Resultados de la búsqueda binaria por {clave} = {valor}:")
                if resultados:
                    for juego in resultados:
                        print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
                else:
                    print("No se encontraron resultados.")
        elif opcion == '5':
            clave = input("Ingrese la clave por la que desea buscar (titulo, anio, puntaje): ")
            valor = input(f"Ingrese el valor de {clave} que desea buscar: ")
            if clave in ['titulo', 'anio', 'puntaje']:
                if clave == 'anio':
                    valor = int(valor)
                resultados = busqueda_lineal(juegos_ordenados, clave, valor)
                print(f"Resultados de la búsqueda lineal por {clave} = {valor}:")
                if resultados:
                    for juego in resultados:
                        print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
                else:
                    print("No se encontraron resultados.")
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue
        
menu()