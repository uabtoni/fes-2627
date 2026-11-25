consum = {"mobil": 12.5, "portatil": 30.2, "tablet": 8.0, "tv": 45.7}

total = 0
for dispositiu in consum:
    total += consum[dispositiu]

print("Consum total:", total, "GB")

nom = input("De quin dispositiu vols saber el consum? ")
if nom in consum:
    print(f"El {nom} ha consumit {consum[nom]} GB")
else:
    print("Aquest dispositiu no existeix")
