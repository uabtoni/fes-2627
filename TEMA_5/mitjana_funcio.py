def calcular_mitjana(llista):
    total = 0
    for valor in llista:
        total += valor
    return total / len(llista)


latencies = [20, 35, 18, 42, 25]
print("Latència mitjana:", calcular_mitjana(latencies), "ms")
