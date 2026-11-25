estudiant = {
    "nom": "Antonio",
    "edat": 19,
    "assignatures": ["Programació", "Xarxes", "Càlcul"]
}
print(estudiant)

print("Segona assignatura:", estudiant["assignatures"][1])
estudiant["edat"] = 20

estudiant["grau"] = "Telecomunicacions"
del estudiant["edat"]
print(estudiant)

print("nom" in estudiant)
print("email" in estudiant)
