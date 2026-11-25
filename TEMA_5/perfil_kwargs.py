def mostrar_dades(**dades):
    for clau, valor in dades.items():
        print(f"{clau}: {valor}")


mostrar_dades(nom="Antonio", edat=20, grau="Telecomunicacions")
