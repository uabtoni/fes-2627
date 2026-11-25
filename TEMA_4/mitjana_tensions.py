tensions = [3.2, 3.3, 3.1, 3.4, 3.3, 3.0]
suma = 0

for t in tensions:
    suma = suma + t

mitjana = suma / len(tensions)
print(f"La tensió mitjana és {round(mitjana, 2)} V")
