n = int(input("Introdueix un número enter positiu N: "))
num = 2

while num <= n:
    es_primer = True
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            es_primer = False
        divisor = divisor + 1
    if es_primer:
        print(num)
    num = num + 1