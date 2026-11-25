enviats = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
rebuts = [0, 1, 0, 0, 1, 1, 0, 1, 0, 0]
errors = 0

for i in range(len(enviats)):
    if enviats[i] != rebuts[i]:
        errors = errors + 1

taxa = errors / len(enviats)
print("Bits erronis:", errors)
print("Taxa d'error:", taxa)
