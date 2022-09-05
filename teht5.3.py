Kokonaisluku = int(input("Anna kokonaisluku: "))
n = 2
found = 0
while found == 0:
    if Kokonaisluku % n == 0 and n != Kokonaisluku:
        found = 1
        print(f"Luku {Kokonaisluku} ei ole alkuluku")
    elif n == 100:
        print(f"Luku {Kokonaisluku} on alkuluku")
        break
    else:
        n += 1
print("Toimenpide on ohi")