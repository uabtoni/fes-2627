los_ences = input("L'indicador LOS està encès? (si/no): ")
internet_ences = input("L'indicador d'Internet està encès? (si/no): ")

if los_ences == "si":
    print("Cal revisar el cable de fibra.")
elif internet_ences == "no":
    print("Cal comprovar el servei del proveïdor.")
else:
    print("La connexió sembla funcionar correctament.")