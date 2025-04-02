word = input("Ingrese una frase o palabra:")

ultima_letra = word[-1]

if ultima_letra == "a" or ultima_letra == "e" or ultima_letra == "i" or ultima_letra == "o" or ultima_letra == "U":
    print(word + "!")
else:
    print(word)