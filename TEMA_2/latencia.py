latencia = float(input("Introdueix la latència en ms: "))
perdua = float(input("Introdueix el percentatge de paquets perduts: "))

if latencia < 0 or perdua < 0 or perdua > 100:
    print("Dades introduïdes no vàlides.")
elif latencia <= 30 and perdua <= 1:
    print("Connexió excel·lent.")
elif latencia <= 80 and perdua <= 3:
    print("Connexió bona.")
elif latencia <= 150 and perdua <= 5:
    print("Connexió acceptable.")
else:
    print("Connexió deficient.")