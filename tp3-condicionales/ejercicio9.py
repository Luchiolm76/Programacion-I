mag = int(input("Ingrese la magnitud del terremoto:"))

if mag <3:
    print("Muy leve")
elif mag >= 3 and mag <4:
    print("Leve")
elif mag >=4 and mag <5:
    print("Moderado") 
elif mag >=5 and mag <6:
    print("Fuerte")
elif mag >=6 and mag <7:
    print("Muy fuerte")
elif mag >=7:
    print("Extremo")
