afstand = 244
dieselprijs = float(input("wat is de diesel prijs vandaag  "))
totaldiesel = afstand / 12 * dieselprijs * 2 / 4 
print ("je moet $",(round(totaldiesel + 8, 2)), " betalen")
#simpel materialen
totalmaterial = 0
pemmincan = 6*5 *3.45 /4
vijgen = 3*5 * 1.24
bescuit = 2 * 2.67
firesteels = 3.26 *2
lucifers = 0.21 * 5
vuursteen = 2.23 * 4
touw = 20 / 10 * 0.59 
totalmaterial += pemmincan  + vijgen + bescuit + lucifers + firesteels + vuursteen + touw

print("het total : $",round(totalmaterial, 2))

#vragen
beer = 0
vos = 0
bever = 0
uil =0 

gef = "gefeliciteerd je kan als "

beer1 = int(input("hoeveel kilogram kunt u tillen? "))
beer2 = int(input("wat is de grootste spijker dat u kunt buigen in mm? "))
vos1 = int(input("wat is uw IQ? "))
vos2 = int(input("hoe snel kunt u een IKEA Larsfrid buffetkast in elkaar zetten zonder handleiding in seconden? "))
bever1 = int(input('wat is het verste dat u kunt springen in aantal seconden? '))
bever2 = int(input('In hoeveel seconde kunt u met een vuursteen vuur maken? '))
uil1 = int(input('hoeveel eetbaren paddestoelen kunt u herkennen? '))
uil2 = int(input('hoeveel giftige kruiden kunt u herkennen? '))

if beer1 >= 100  and beer2 >= 10:
    beer == True
elif beer1 < 100 and beer2 < 10:
    beer == False
if vos1 >= 130 and vos2 <= 60:
    vos = True
elif vos1 < 130 and vos2 > 60:
    vos= False 
if bever1 >= 3 and bever2 <= 60:
    bever = True
elif bever1 < 3 and bever2 > 60:
    bever = False
if uil1 >= 10 and uil2 >= 20:
    uil = True
elif uil1 < 10 and uil2 < 20:
    uil = False

if beer == True:
    print("gefeliciteerdt, je kan als beer mee doen")
elif beer == False:
    print(gef, "beer meedoen")
if vos == True:
    print(gef, "vos meedoen")
elif vos == False:
    print()
if bever == True:
    print(gef,"bever meedoen")
elif bever == False:
    print()
if uil == True:
    print(gef,"uil meedoen")
elif uil == False:
    print()

x = totalmaterial / 5 + totaldiesel
eindvraag = int(input("hoeveel bent u bereid om te betalen voor de buscraft?  "))
if eindvraag >= x:
    print("gefeliciteerd je mag mee doen")
elif eindvraag < x:
    print("sorry, je mag niet mee doen? ")
else:
    print("sorry dat begrijp ik niet")