def nopanheitto(arvo):
    heiton_arvo = 0
    heittolkm = 0
    while heiton_arvo != arvo:
        heiton_arvo = random.randint(1, arvo)
        nopanheitot.append(heiton_arvo)
        heittolkm += 1
    print(f"Noppien luvuiksi tuli: {nopanheitot}")
    print(f"Noppia joutui heittämään {heittolkm} kappaletta.")
    return

import random
tahkot = int(input("Kuinka monta tahkoa nopassa on?\n"))
nopanheitot = []
nopanheitto(tahkot)