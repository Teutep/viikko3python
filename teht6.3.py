def gallons(nestegallonat):
        litrat = nestegallonat / 4.54609
        return print(f"Gallonit {nestegallonat} litroissa on {litrat}")

gallon = 0
while gallon >= 0:
    gallon = float(input("Kuinka monta gallonaa haluat muuttaa litroiksi?\n"))
    gallons(gallon)