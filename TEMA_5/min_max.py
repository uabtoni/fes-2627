def min_max(numeros):
    return min(numeros), max(numeros)


senyals = [-67, -54, -80, -49, -72]
minim, maxim = min_max(senyals)
print("Senyal mínim:", minim)
print("Senyal màxim:", maxim)
