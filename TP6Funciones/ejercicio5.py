def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal
segundos = int(input("Ingrese cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")
