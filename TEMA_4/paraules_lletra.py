dispositius = ["router", "switch", "repetidor", "servidor", "Ruter", "modem"]
lletra = input("Introdueix una lletra: ").lower()
total = 0

for d in dispositius:
    if d.lower().startswith(lletra):
        total += 1

print(f"Hi ha {total} dispositius que comencen per '{lletra}'")
