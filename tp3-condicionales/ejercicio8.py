nombre = input("Ingrese su nombre:")

print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la primera letra en mayúscula")

opcion = input("Ingresa la opcion que quieras:")

if opcion == "1":
    print("Tu nombre en MAYUSCULAS es:", nombre.upper())
elif opcion == "2": 
    print("Tu nombre en minusculas es:", nombre.lower())
elif opcion == "3":
    print("Tu nombre con la primera letra en mayuscula es:", nombre.capitalize())