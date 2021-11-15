afstand = 244
dieselprijs = float(input("wat is de diesel prijs vandaag  "))
totalprijs = afstand / 12 * dieselprijs * 2 + 8

print ("je moet $",str(round(totalprijs, 2)), " betalen")
