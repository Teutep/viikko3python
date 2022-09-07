#Arpakuutioiden kvanti- ja kvaliteetti
import random
Arpakuutio = int(input("Kuinka monta arpakuutiota?\n"))
Arvo = 0
for x in range(0, Arpakuutio):
    Arvo += random.randint(1, 6)
print(f"Heitettyjä noppia on {Arpakuutio} ja näiden noppien summa on {Arvo}")