def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal
temp_c = float(input("Temperatura en °C: "))
temp_f = celsius_a_fahrenheit(temp_c)
print(f"{temp_c}°C equivale a {temp_f:.2f}°F")
