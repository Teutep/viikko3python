def gallons(nestegallonat):
        litrat = nestegallonat * 3.78541
        return print(f"{nestegallonat:.2f} nestegallonaa on {litrat:.2f} litraa")

gallon = 0
while gallon >= 0:
    gallon = float(input("Kuinka monta gallonaa haluat muuttaa litroiksi?\n"))
    gallons(gallon)