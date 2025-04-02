contraseña = str(input("Ingrese una contraseña de entre 8 y 14 caracteres incluyendo 8 y 14:"))

if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("INgresaste la contraseña correcta")
else:
    print("La contraseña debe tener de entre 8 y 14 caracteres")