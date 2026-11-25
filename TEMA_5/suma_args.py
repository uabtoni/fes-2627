def sumar(*numeros):
    resultat = 0
    for n in numeros:
        resultat += n
    return resultat


print(sumar(3, 7))
print(sumar(1, 2, 3, 4, 5))
print(sumar(10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
