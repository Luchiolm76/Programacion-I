# Esta es la lista de videojuegos que me tiro chat, con el nombre, año, genero y puntuacion
videojuegos = [
    {"nombre": "The Witcher 3", "año": 2015, "género": "RPG", "puntuación": 9.5},
    {"nombre": "Minecraft", "año": 2011, "género": "Sandbox", "puntuación": 9.2},
    {"nombre": "Fortnite", "año": 2017, "género": "Battle Royale", "puntuación": 8.3},
    {"nombre": "GTA V", "año": 2013, "género": "Acción", "puntuación": 9.0},
    {"nombre": "Celeste", "año": 2018, "género": "Plataformas", "puntuación": 8.8},
    {"nombre": "God of War", "año": 2018, "género": "Acción", "puntuación": 9.7},
    {"nombre": "Red Dead Redemption 2", "año": 2018, "género": "Aventura", "puntuación": 9.6},
    {"nombre": "The Legend of Zelda: Breath of the Wild", "año": 2017, "género": "Aventura", "puntuación": 9.8},
    {"nombre": "Hollow Knight", "año": 2017, "género": "Metroidvania", "puntuación": 9.0},
    {"nombre": "Dark Souls III", "año": 2016, "género": "RPG", "puntuación": 8.9}
]
def ordenar_por_puntuacion(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lista[j]["puntuación"] < lista[j + 1]["puntuación"]:
                # Intercambiar los juegos
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
# Llamas a la función de ordenamiento
ordenar_por_puntuacion(videojuegos)

# Y luego mostramos la lista ordenada
print("🎮 Videojuegos ordenados por puntuación (de mayor a menor):")
for juego in videojuegos:
    print(f"{juego['nombre']} - {juego['puntuación']}")


