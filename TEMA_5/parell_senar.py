def es_parell(n):
    return n % 2 == 0


num = int(input("Introdueix un número: "))
if es_parell(num):
    print(num, "és parell")
else:
    print(num, "és senar")
