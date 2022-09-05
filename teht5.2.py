luvut = [] #Listan define
luku = input("Anna luku: ") #Annetaan arvo stringina
while luku != "": #Loopataan kun arvo ei ole tyhja
    luvut.append(int(luku)) #Luvut listataan kokonaislukuina stringin sijaan
    luku = (input("Anna luku: ")) #Uusiokysely stringina
luvut.sort(reverse=True) #Listaus suuremmasta pienempaan
print(f"{luvut[0:5]}") #Tulostus tapahtuu listan viiden ensimmaisen mukaan