def taula(numero, fins=10):
    for i in range(1, fins + 1):
        print(f"{numero} x {i} = {numero * i}")


taula(7)
print()
taula(3, 5)
