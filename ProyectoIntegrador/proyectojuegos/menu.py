from functions import bubble_sort, quick_sort, busqueda_binaria, busqueda_lineal
from listajuegos import juegos



#Menu principal del programa de juegos
def menu():

    juegos_ordenados = juegos[:] #copia de la lista original para no modificarla
    
    print("Bienvenido al programa de juegos")
    print("1. Mostrar lista de juegos")
    print("2. Hacer ordenamiento de juegos por burbuja")                ####OPCIONES DEL MENU
    print("3. Hacer ordenamiento de juegos rapido")
    print("4. Buscar un juego con busqueda binaria") 
    print("5. Buscar un juego con busqueda lineal") 
    print("6. Salir") 
    
    #entramos al bucle del menu
    while True:
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            for juego in juegos_ordenados: #recorremos la lista de juegos y mostramos sus detalles
                print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
        elif opcion == '2':
            print("Has seleccionado ordenar la lista de juegos por burbuja.")
            print("================================================")
            key = input("¿Por qué clave desea ordenar? titulo/anio/puntaje: ")
            juegos_ordenados = bubble_sort(juegos_ordenados, key.lower()) #llamamos a la funcion de ordenamiento por burbuja
            #mostramos los juegos ordenados
            print("Lista ordenada por burbuja.")
            for juego in juegos_ordenados: #recorremos la lista de juegos y mostramos sus detalles
                print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
        elif opcion == '3':
            print("Has seleccionado ordenar la lista de juegos con quicksort.")
            print("================================================")
            key = input("¿Por qué clave desea ordenar? titulo/anio/puntaje: ") #aca medimos la clave por la que se ordenara
            juegos_ordenados = quick_sort(juegos_ordenados, key.lower()) #llamamos a la funcion de ordenamiento rapido y le pasamos la clave
            #mostramos los juegos ordenados
            print("Lista ordenada por quick sort.")
            for juego in juegos_ordenados: #recorremos la lista de juegos y mostramos sus detalles
                print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
        elif opcion == '4':
            print("Has seleccionado busqueda binaria.")
            print("================================================")
            clave = input("Ingrese la clave por la que desea buscar (titulo, anio, puntaje): ") #aca de nuevo pedimos la clave por la que se buscara
            valor = input(f"Ingrese el valor de {clave} que desea buscar: ")
            clave = clave.lower()  # Convertimos la clave a minúsculas para evitar problemas de mayúsculas/minúsculas
            if clave in ['titulo', 'anio', 'puntaje']:
                if clave == 'anio':
                    valor = int(valor)
                    juegos_ordenados = bubble_sort(juegos_ordenados, 'anio')  # Aseguramos que la lista esté ordenada por 'anio'
                elif clave == 'puntaje':
                    valor = int(valor)
                    juegos_ordenados = bubble_sort(juegos_ordenados, 'puntaje')  # Aseguramos que la lista esté ordenada por 'puntaje'
                elif clave == 'titulo':
                    juegos_ordenados = bubble_sort(juegos_ordenados, 'titulo') # Aseguramos que la lista esté ordenada por 'titulo'
                resultados = busqueda_binaria(juegos_ordenados, clave, valor) #busqueda binaria retorna un arr de juegos que coinciden con la clave y el valor
                print(f"Resultados de la búsqueda binaria por {clave} = {valor}:")
                if resultados:
                    for juego in resultados: #recorremos los resultados y mostramos sus detalles
                        print(f"Título: {juego['titulo']}, Año: {juego['anio']}, Puntaje: {juego['puntaje']}")
                else:
                    print("No se encontraron resultados.")
            else:
                print("Clave no válida. Por favor, elija entre 'titulo', 'anio' o 'puntaje'.")
        elif opcion == '5':
            print("Has seleccionado busqueda lineal.")
            print("================================================")
            clave = input("Ingrese la clave por la que desea buscar (titulo, anio, puntaje): ")
            clave = clave.lower()  # Convertimos la clave a minúsculas para evitar problemas de mayúsculas/minúsculas
            valor = int(input(f"Ingrese el valor de {clave} que desea buscar: "))
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
            else:
                print("Clave no válida. Por favor, elija entre 'titulo', 'anio' o 'puntaje'.")
        elif opcion == '6':
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue #si la opcion no es valida, volvemos al inicio del bucle
        
menu()