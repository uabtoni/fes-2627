bateria = float(input("Introdueix el percentatge de bateria del SAI: "))

if bateria < 0 or bateria > 100:
    print("Valor de bateria no vàlid.")
elif bateria < 20:
    print("Nivell crític.")
elif bateria <= 49:
    print("Nivell baix.")
else:
    print("Nivell suficient.")