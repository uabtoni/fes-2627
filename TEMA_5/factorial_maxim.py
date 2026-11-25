def factorial(n):
    resultat = 1
    while n > 1:
        resultat = resultat * n
        n = n - 1
    return resultat


def maxim(llista):
    mes_gran = llista[0]
    for x in llista:
        if x > mes_gran:
            mes_gran = x
    return mes_gran


print("Factorial de 6:", factorial(6))
print("Màxim:", maxim([4, 19, 2, 33, 8]))
