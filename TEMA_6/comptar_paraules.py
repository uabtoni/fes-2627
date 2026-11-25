protocols = ["tcp", "udp", "tcp", "http", "udp", "tcp", "dns", "http"]
comptador = {}

for p in protocols:
    if p in comptador:
        comptador[p] += 1
    else:
        comptador[p] = 1

print(comptador)
