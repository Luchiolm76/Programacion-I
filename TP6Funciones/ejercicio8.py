def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Peso en kg: "))
altura = float(input("Altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc:.2f}")
