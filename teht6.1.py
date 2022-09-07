def nopanheitto():
    heiton_arvo = 0
    while heiton_arvo != 6:
        heiton_arvo = random.randint(1, 6)
        nopanheitot.append(heiton_arvo)
    print(f"Noppien luvuiksi tuli: {nopanheitot}")
    return

import random
nopanheitot = []
nopanheitto()