edad = int(input("Ingrese su edad:"))
if edad < 12:
    print("Eres un niño")
elif edad >= 12 and  edad < 18:
    print("Eres adolescente")
elif edad >= 18 and edad < 30:
    print("Eres un joven o adulto")
elif edad >= 30:
    print("Eres Adulto mayor")