import random
from statistics import mean, median, mode

# Creamos la lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calculamos los valores estadísticos
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

# Mostramos los valores
print("Lista de números aleatorios:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

# Comparamos para detectar el sesgo
if media > mediana and mediana > moda:
    print("Hay sesgo positivo (a la derecha)")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo (a la izquierda)")
else:
    print("No hay sesgo (distribución simétrica)")
