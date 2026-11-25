pings = [23, 45, 12, 67, 34, 29]
maxim = pings[0]

for p in pings:
    if p > maxim:
        maxim = p

print("El ping més alt és:", maxim, "ms")
