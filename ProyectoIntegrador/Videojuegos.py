# modules/display.py

def mostrar_menu():
    print("\n=== Menú Principal ===")
    print("1. Ver todos los juegos")
    print("2. Ordenar juegos")
    print("3. Buscar un juego")
    print("4. Salir")
    return input("Elige una opción: ")

def mostrar_juegos(lista):
    print("\n--- Lista de Juegos ---")
    for juego in lista:
        print(f"{juego['nombre']} | {juego['anio']} | {juego['puntaje']} pts")
