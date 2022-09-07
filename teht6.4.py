def listaus(numero):
    summaus = sum(numero)
    return summaus

lista = []
Loop = int(input("Kuinka monta kokonaislukua haluat antaa? "))
for x in range(0, Loop):
    Tulos = int(input("Anna kokonaisluku: "))
    lista.append(Tulos)
listaus(lista)
print(f"Kokonaislukujen summa on: {listaus(lista)}")