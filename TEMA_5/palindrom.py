def es_palindrom(paraula):
    paraula = paraula.lower()
    return paraula == paraula[::-1]


print(es_palindrom("Radar"))
print(es_palindrom("router"))
print(es_palindrom("Anna"))
