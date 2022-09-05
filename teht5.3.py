Kokonaisluku = int(input("Anna kokonaisluku: "))
Lista = []
n = 2
found = 0
while found == 0:
    if Kokonaisluku % n == 0 and n != Kokonaisluku:
        found = 1
        print(f"Luku {Kokonaisluku} ei ole alkuluku")
        nm = Kokonaisluku % n
    elif n == 10:
        print(f"Luku {Kokonaisluku} on alkuluku")
        nm = Kokonaisluku % n
        break
    else:
        n += 1
        nm = Kokonaisluku % n
print(f"Toimenpide on ohi")