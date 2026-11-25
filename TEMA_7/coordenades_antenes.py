antenes = [("A1", 41.50, 2.10), ("A2", 41.39, 2.17), ("A3", 41.98, 2.82)]

for nom, lat, lon in antenes:
    print(f"Antena {nom}: latitud {lat}, longitud {lon}")

ip = (192, 168, 1, 10)
a, b, c, d = ip
print(f"Xarxa: {a}.{b}.{c}.0")
