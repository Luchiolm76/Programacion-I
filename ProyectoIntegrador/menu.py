import functions

def menu():
    print("Bienvenido al programa de buscador de juegos")
    print("1. Buscar juego por nombre")
    print("2. Buscar juego por año")
    print("3. Buscar juego por puntaje")
    
    while True:
        opcion = input("Seleccione una opción (1-3): ")
        if opcion == '1':
            functions.buscar_juego_por_nombre()
        elif opcion == '2':
            functions.buscar_juego_por_anio()
        elif opcion == '3':
            functions.buscar_juego_por_puntaje()
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
            continue