def comptar_vocals(text):
    vocals = "aeiou"
    comptador = 0
    for lletra in text.lower():
        if lletra in vocals:
            comptador += 1
    return comptador


frase = input("Escriu una frase: ")
print("Vocals:", comptar_vocals(frase))
