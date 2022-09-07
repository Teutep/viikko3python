def parilliset(laskettavat):
    parilliset = []
    for n in laskettavat:
        if n % 2 == 0:
            parilliset.append(n)
    return parilliset

lista = []
lkm = int(input("Kuinka monta kokonaislukua listataan? "))
for x in range(0, lkm):
    luku = int(input("Anna kokonaisluku: "))
    lista.append(luku)
print(f"Kaikki luvut: {lista}")
parilliset(lista)
print(f"Parilliset luvut: {parilliset(lista)}")