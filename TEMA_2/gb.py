consum_gb = float(input("Introdueix el consum de dades en GB: "))
pla_gb = 20.0

if consum_gb <= pla_gb:
    print("El consum està dins del límit.")
else:
    gb_extra = consum_gb - pla_gb
    print(f"S'ha superat el límit per {gb_extra} GB addicionals.")