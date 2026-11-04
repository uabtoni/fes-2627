suma = 0
numero = int(input("Introdueix un número (0 per acabar): "))

while numero != 0:
    suma = suma + numero
    numero = int(input("Introdueix un número (0 per acabar): "))

print("La suma total és:", suma)