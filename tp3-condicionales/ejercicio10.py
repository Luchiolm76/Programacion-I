hemf = input("¿En qué hemisferio se encuentra? (N o S): ").upper()
mes = input("¿Qué mes del año es?: ").capitalize()
dia = int(input("¿Qué día es?: "))

if hemf == "N":
    if (mes == "Diciembre" and dia >= 21) or mes in ["Enero", "Febrero"] or (mes == "Marzo" and dia <= 20):
        print("Usted se encuentra en Invierno")
    elif (mes == "Marzo" and dia >= 21) or mes in ["Abril", "Mayo"] or (mes == "Junio" and dia <= 20):
        print("Usted se encuentra en Primavera")
    elif (mes == "Junio" and dia >= 21) or mes in ["Julio", "Agosto"] or (mes == "Septiembre" and dia <= 20):
        print("Usted se encuentra en Verano")
    elif (mes == "Septiembre" and dia >= 21) or mes in ["Octubre", "Noviembre"] or (mes == "Diciembre" and dia <= 20):
        print("Usted se encuentra en Otoño")
elif hemf == "S":
    if (mes == "Diciembre" and dia >= 21) or mes in ["Enero", "Febrero"] or (mes == "Marzo" and dia <= 20):
        print("Usted se encuentra en Verano")
    elif (mes == "Marzo" and dia >= 21) or mes in ["Abril", "Mayo"] or (mes == "Junio" and dia <= 20):
        print("Usted se encuentra en Otoño")
    elif (mes == "Junio" and dia >= 21) or mes in ["Julio", "Agosto"] or (mes == "Septiembre" and dia <= 20):
        print("Usted se encuentra en Invierno")
    elif (mes == "Septiembre" and dia >= 21) or mes in ["Octubre", "Noviembre"] or (mes == "Diciembre" and dia <= 20):
        print("Usted se encuentra en Primavera")
else:
    print("Hemisferio no válido")