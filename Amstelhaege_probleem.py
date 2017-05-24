
import random
from math import sqrt
from random import randint
from tkinter import *
import Woning
import matplotlib.pyplot as plt
import random

#random.seed(3)

vergrotingHuizen = 3

width = 160
height = 180
oppervlakte = width * height
hoeveelHuizen = [20, 40, 60]
maxHuizen = 60  #random.choice(hoeveelHuizen)
woningen = []
besteWoningen = []
hoogstewaarde = 0
hoogstewaardes = []
iteraties = []
xas = []
yas = []

def coordinatenValid(x, y, breedte, diepte):
    coordinatenValid = True
    for woning in woningen:
        if x >= (woning.linksBovenX - breedte - woning.vrijeruimte) \
        and x <= (woning.linksBovenX + woning.breedte + woning.vrijeruimte) \
        and y >= (woning.linksBovenY - diepte - woning.vrijeruimte) \
        and y <= (woning.linksBovenY + woning.diepte + woning.vrijeruimte):
            coordinatenValid = False
    return coordinatenValid

def vindCoordinaten(typeWoning):
    breedte = typeWoning.breedte
    diepte = typeWoning.diepte
    randomX = randint(typeWoning.vrijeruimte, int(width - breedte - typeWoning.vrijeruimte))
    randomY = randint(typeWoning.vrijeruimte, int(height - diepte - typeWoning.vrijeruimte))
    while not coordinatenValid(randomX, randomY, typeWoning.breedte, typeWoning.diepte):
        randomX = randint(typeWoning.vrijeruimte, int(width - breedte - typeWoning.vrijeruimte))
        randomY = randint(typeWoning.vrijeruimte, int(height - diepte - typeWoning.vrijeruimte))
    nieuwCoordinaat = [randomX, randomY]
    return nieuwCoordinaat


def vrijstandTussen(woningA, woningB):
    if woningA is Woning.Single or Woning.Bungalo or Woning.Maison and woningB is Woning.Single or Woning.Bungalo or Woning.Maison:
        left = woningB.rechtsOnderX < woningA.linksOnderX
        right = woningA.rechtsOnderX < woningB.linksOnderX
        bottom = woningA.rechtsOnderY < woningB.rechtsBovenY
        top = woningB.rechtsOnderY < woningA.rechtsBovenY

        if top and left:
            euclidean_distance = sqrt((woningA.linksBovenX - woningB.rechtsOnderX) ** 2 + (woningA.linksBovenY - woningB.rechtsOnderY) ** 2)
            return euclidean_distance
        elif left and bottom:
            euclidean_distance = sqrt((woningA.linksOnderX - woningB.rechtsBovenX) ** 2 + (woningA.linksOnderY - woningB.rechtsBovenY) ** 2)
            return euclidean_distance
        elif bottom and right:
            euclidean_distance = sqrt((woningA.rechtsOnderX - woningB.linksBovenX) ** 2 + (woningA.rechtsOnderY - woningB.linksBovenY) ** 2)
            return euclidean_distance
        elif right and top:
            euclidean_distance = sqrt((woningA.rechtsBovenX - woningB.linksOnderX) ** 2 + (woningA.rechtsBovenY - woningB.linksOnderY) ** 2)
            return euclidean_distance
        elif left:
            euclidean_distance = abs(woningA.linksBovenX - woningB.rechtsBovenX)
            return euclidean_distance
        elif right:
            euclidean_distance = abs(woningA.rechtsBovenX - woningB.linksBovenX)
            return euclidean_distance
        elif bottom:
            euclidean_distance = abs(woningA.linksOnderY - woningB.linksBovenY)
            return euclidean_distance
        elif top:
            euclidean_distance = abs(woningA.linksBovenY - woningB.linksOnderY)
            return euclidean_distance


def plaatsWoning(typeWoning):
    nieuwCoordinaat = vindCoordinaten(typeWoning)
    x = nieuwCoordinaat[0]
    y = nieuwCoordinaat[1]
    woning = typeWoning(x, y)
    woningen.append(woning)
    return woning


def tekenWoningen(woningen):
    for woning in woningen:
        index = woningen.index(woning)
        map.create_rectangle(woning.linksBovenX * vergrotingHuizen, woning.linksBovenY * vergrotingHuizen,
                             (woning.linksBovenX + woning.breedte) * vergrotingHuizen ,
                             (woning.linksBovenY + woning.diepte) * vergrotingHuizen , fill = woning.kleur)
        map.create_text((woning.linksBovenX+4) * vergrotingHuizen, (woning.linksBovenY+3.5) * vergrotingHuizen, text= index, font="Times 18 italic")


def berekenVrijstandWoning(woningen, woningIndex):
    shortest_euclidean_distance = 241 * vergrotingHuizen
    for j in range (int(maxHuizen - 1)):
        if j != woningIndex:
            if woningen[woningIndex] is not Woning.Water and woningen[j] is not Woning.Water:
                if vrijstandTussen(woningen[woningIndex], woningen[j]) < shortest_euclidean_distance:
                    shortest_euclidean_distance = vrijstandTussen(woningen[woningIndex], woningen[j])
    #print(shortest_euclidean_distance)
    return shortest_euclidean_distance

def berekenKaartWaarde(woningen):
    waardeKaart = 0
    for woning in woningen:
        index = int(woningen.index(woning))
        shortest_euclidean_distance = berekenVrijstandWoning(woningen, index)
        waardeKaart = waardeKaart + woning.waarde + woning.waarde * ((shortest_euclidean_distance - woning.vrijeruimte) * woning.waardeStijging)
    return waardeKaart

def mutateMap(woningen):
    oudeKaartWaarde = berekenKaartWaarde(woningen)
    wijzigWoningNummer = randint(0, maxHuizen)
    wijzigWoning = woningen[wijzigWoningNummer]
    verschuivingX = randint(-3, 3)
    verschuivingY = randint(-3, 3)
    wijzigWoning.linksBovenX += verschuivingX
    wijzigWoning.linksBovenY += verschuivingY
    del woningen[wijzigWoningNummer]
    if (wijzigWoning.linksBovenX + wijzigWoning.breedte) > width or \
        0 > wijzigWoning.linksBovenX or \
        (wijzigWoning.linksBovenY + wijzigWoning.diepte) > height \
        or 0 > wijzigWoning.linksBovenY or not coordinatenValid(wijzigWoning.linksBovenX, wijzigWoning.linksBovenY, wijzigWoning.breedte, wijzigWoning.diepte):
            wijzigWoning.linksBovenX -= verschuivingX
            wijzigWoning.linksBovenY -= verschuivingY
            cancelled = True
    else:
        cancelled = False
    woningen.insert(wijzigWoningNummer, wijzigWoning)
    if oudeKaartWaarde > berekenKaartWaarde(woningen) and not cancelled:
        wijzigWoning.linksBovenX -= verschuivingX
        wijzigWoning.linksBovenY -= verschuivingY
    return woningen


def houseSwap():
    water = int(Woning.Water.aantalWatereenheden)
    indexhuis1 = randint(0 + water, maxHuizen + water - 1) # (maxHuizen + Woning.Water.aantalWatereenheden))
    while True:
        indexhuis2 = randint(0 + water, maxHuizen + water - 1)
        if indexhuis1 != indexhuis2: break

    huis1 = woningen[indexhuis1]
    huis2 = woningen[indexhuis2]
    huidigeX1 = huis1.linksBovenX
    huidigeY1 = huis1.linksBovenY
    huidigeX2 = huis2.linksBovenX
    huidigeY2 = huis2.linksBovenY

    nieuweX1 = huidigeX2
    nieuweY1 = huidigeY2
    nieuweX2 = huidigeX1
    nieuweY2 = huidigeY1

    if (coordinatenValid(nieuweX1,nieuweY1,huis1.breedte,huis1.diepte) and coordinatenValid(nieuweX2,nieuweY2,huis2.breedte,huis2.diepte)):
        huis1.linksBovenX = nieuweX1
        huis1.linksBovenY = nieuweY1
        huis2.linksBovenX = nieuweX2
        huis2.linksBovenY = nieuweY2
    return woningen

def conduct():
    for i in range(int(Woning.Water.aantalWatereenheden)):
        plaatsWoning(Woning.Water)
    for j in range(int(Woning.Maison.aandeelHuizen * maxHuizen)):
        plaatsWoning(Woning.Maison)
    for k in range(int(Woning.Bungalo.aandeelHuizen * maxHuizen)):
        plaatsWoning(Woning.Bungalo)
    for l in range(int(Woning.Single.aandeelHuizen * maxHuizen)):
        plaatsWoning(Woning.Single)
    berekenKaartWaarde(woningen)

#HEURISTIEKEN

def randomSampling(n):

    for i in range(n):
        conduct()
        global waardeKaart
        global hoogstewaarde
        global woningen
        global besteWoningen
        if waardeKaart > hoogstewaarde:
            hoogstewaarde = waardeKaart
            besteWoningen = woningen
        yas.append(hoogstewaarde)
        xas.append(i)
        waardeKaart = 0
        woningen = []

    return besteWoningen


def hillClimber(n):
    conduct()
    global woningen
    for i in range (n):
        mutateMap(woningen)
        yas.append(berekenKaartWaarde(woningen))
        xas.append(i)
    global hoogstewaarde
    global besteWoningen
    besteWoningen = woningen
    hoogstewaarde = berekenKaartWaarde(woningen)
    for woning in woningen:
        print(int(woningen.index(woning)), woning.linksBovenX, woning.linksBovenY)
    return besteWoningen


def hillClimber2(n):
    conduct()
    global woningen
    useWoningenWaarde = berekenKaartWaarde(woningen)
    print("Beginwaarde =", useWoningenWaarde)
    for i in range(n):
        testWoningen = houseSwap()
        testWoningenWaarde = berekenKaartWaarde(testWoningen)
        if testWoningenWaarde >= useWoningenWaarde:
            woningen = testWoningen
            useWoningenWaarde = testWoningenWaarde
    global hoogstewaarde
    global besteWoningen
    hoogstewaarde = useWoningenWaarde
    print("Hoogstewaarde = ", hoogstewaarde)
    besteWoningen = woningen
    return woningen

#UITVOEREN
hillClimber(10000)
print("De waarde van de beste kaart is ", hoogstewaarde)


plt.plot(xas, yas)
plt.title('Kaartwaarde', fontsize=20)
plt.xlabel('Iteraties', fontsize=16)
plt.ylabel('Waarde in €', fontsize=16)
plt.show()

#visualiseren
master = Tk()

map = Canvas(master, width=width * vergrotingHuizen, height=height * vergrotingHuizen)
map.pack()

tekenWoningen(woningen)
#waardeKaartBerekenen(woningen)
tekenWoningen(besteWoningen)
print("#klaarmettekenen")
mainloop()



#show()