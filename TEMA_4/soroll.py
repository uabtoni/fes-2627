nivells_soroll = [-90, -83, -77, -96, -79, -85, -74]
llindar = -80
comptador = 0

for nivell in nivells_soroll:
    if nivell > llindar:
        comptador = comptador + 1

print(f"Hi ha {comptador} mostres per sobre de {llindar} dBm")
