luvut = []
luku = input("Anna luku: ")
while luku != "":
    luvut.append(int(luku))
    luku = (input("Anna luku: "))
luvut.sort(reverse=True)
print(f"{luvut[0:5]}")