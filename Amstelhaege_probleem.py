
import random
from math import sqrt
from random import randint
from tkinter import *
import Woning
#import matplotlib.pyplot as plt
import random

#random.seed(3)

vergrotingHuizen = 3

width = 160
height = 180
oppervlakte = width * height
hoeveelHuizen = [20, 40, 60]
maxHuizen = 20  #random.choice(hoeveelHuizen)
woningen = []
besteWoningen = []
waardeKaart = 0
hoogstewaarde = 0
hoogstewaardes = []
iteraties = []

def coordinatenValid(randomX, randomY, breedte, diepte):
    coordinatenValid = True
    for woning in woningen:
        if randomX >= (woning.linksBovenX - breedte - woning.vrijeruimte) \
        and randomX <= (woning.linksBovenX + woning.breedte + woning.vrijeruimte) \
        and randomY >= (woning.linksBovenY - diepte - woning.vrijeruimte) \
        and randomY <= (woning.linksBovenY + woning.diepte + woning.vrijeruimte):
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
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from top and left")
            return euclidean_distance
        elif left and bottom:
            euclidean_distance = sqrt((woningA.linksOnderX - woningB.rechtsBovenX) ** 2 + (woningA.linksOnderY - woningB.rechtsBovenY) ** 2)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from left and bottom")
            return euclidean_distance
        elif bottom and right:
            euclidean_distance = sqrt((woningA.rechtsOnderX - woningB.linksBovenX) ** 2 + (woningA.rechtsOnderY - woningB.linksBovenY) ** 2)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from bottom and right")
            return euclidean_distance
        elif right and top:
            euclidean_distance = sqrt((woningA.rechtsBovenX - woningB.linksOnderX) ** 2 + (woningA.rechtsBovenY - woningB.linksOnderY) ** 2)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from right and top")
            return euclidean_distance
        elif left:
            euclidean_distance = abs(woningA.linksBovenX - woningB.rechtsBovenX)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from left")
            return euclidean_distance
        elif right:
            euclidean_distance = abs(woningA.rechtsBovenX - woningB.linksBovenX)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from right")
            return euclidean_distance
        elif bottom:
            euclidean_distance = abs(woningA.linksOnderY - woningB.linksBovenY)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from bottom")
            return euclidean_distance
        elif top:
            euclidean_distance = abs(woningA.linksBovenY - woningB.linksOnderY)
            #print("euclidean distance between", woningen.index(woningA), "and", woningen.index(woningB), "=", euclidean_distance, "\n", "distance is measured from top")
            return euclidean_distance
        #print(woningA.linksBovenX, woningA.linksBovenY, woningB.linksBovenX, woningB.linksBovenY)


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
        map.create_rectangle(woning.linksBovenX * vergrotingHuizen, woning.linksBovenY * vergrotingHuizen, (woning.linksBovenX + woning.breedte) * vergrotingHuizen , (woning.linksBovenY + woning.diepte) * vergrotingHuizen , fill = woning.kleur)
        map.create_text((woning.linksBovenX+4) * vergrotingHuizen, (woning.linksBovenY+3.5) * vergrotingHuizen, text= index, font="Times 18 italic")


def berekenVrijstandWoning(woningen, woning):
    shortest_euclidean_distance = 241 * vergrotingHuizen
    for j in range (int(maxHuizen - 1)):
        if j != woning:
            if woning is Woning.Single or Woning.Bungalo or Woning.Maison and woningen[j] is Woning.Single or Woning.Bungalo or Woning.Maison:
                if vrijstandTussen(woningen[woning], woningen[j]) < shortest_euclidean_distance:
                    shortest_euclidean_distance = vrijstandTussen(woningen[woning], woningen[j])
    #print(shortest_euclidean_distance)
    return shortest_euclidean_distance

def berekenKaartWaarde(woningen):
    for woning in woningen:
        index = int(woningen.index(woning))
        shortest_euclidean_distance = berekenVrijstandWoning(woningen, index)
        global waardeKaart
        waardeKaart = waardeKaart + woning.waarde + woning.waarde * ((shortest_euclidean_distance - woning.vrijeruimte) * woning.waardeStijging)
    return waardeKaart

def mutateMap():
    wijzigWoningNummer = randint(0, maxHuizen)
    wijzigWoning = woningen[wijzigWoningNummer]
    verschuivingX = randint(-3, 3)
    verschuivingY = randint(-3, 3)
    wijzigWoning.linksBovenX = wijzigWoning.linksBovenX + verschuivingX
    wijzigWoning.linksBovenY = wijzigWoning.linksBovenY + verschuivingY
    woningen.remove(wijzigWoning)
    while not (coordinatenValid(wijzigWoning.linksBovenX, wijzigWoning.linksBovenY, wijzigWoning.breedte, wijzigWoning.diepte) or (wijzigWoning.linksBovenX - wijzigWoning.breedte - wijzigWoning.vrijeruimte) < width or 0 > (wijzigWoning.linksBovenX - wijzigWoning.vrijeruimte) or 0 > (wijzigWoning.linksBovenY - wijzigWoning.diepte-wijzigWoning.vrijeruimte) < height) or 0 > (wijzigWoning.linksBovenY - wijzigWoning.vrijeruimte):
        verschuivingX = randint(-3, 3)
        verschuivingY = randint(-3, 3)
        wijzigWoning.linksBovenX = wijzigWoning.linksBovenX + verschuivingX
        wijzigWoning.linksBovenY = wijzigWoning.linksBovenY + verschuivingY
    woningen.append(wijzigWoning)
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
        hoogstewaardes.append(hoogstewaarde)
        iteraties.append(i)
        waardeKaart = 0
        woningen = []

    return besteWoningen


def hillClimber(n):
    conduct()
    global woningen
    useWoningenWaarde = berekenKaartWaarde(woningen)
    for i in range (n):
        testWoningen = mutateMap()
        testWoningenWaarde = berekenKaartWaarde(testWoningen)
        if testWoningenWaarde >= useWoningenWaarde:
            woningen = testWoningen
            useWoningenWaarde = testWoningenWaarde
    global hoogstewaarde
    global besteWoningen
    hoogstewaarde = useWoningenWaarde
    besteWoningen = woningen
    return woningen

#UITVOEREN
randomSampling(10000)
print("De waarde van de beste kaart is ", hoogstewaarde)

#plt.plot(iteraties, hoogstewaardes)
#plt.title('Kaartwaarde', fontsize=20)
#plt.xlabel('Iteraties', fontsize=16)
#plt.ylabel('Waarde in €', fontsize=16)
#plt.show()

randomSampling(100)
'''
plt.plot(iteraties, hoogstewaardes)
plt.title('Kaartwaarde', fontsize=20)
plt.xlabel('Iteraties', fontsize=16)
plt.ylabel('Waarde in €', fontsize=16)
plt.show()
'''
#visualiseren
master = Tk()

map = Canvas(master, width=width * vergrotingHuizen, height=height * vergrotingHuizen)
map.pack()

tekenWoningen(woningen)
#waardeKaartBerekenen(woningen)
tekenWoningen(besteWoningen)
print("klaarmettekenen")
mainloop()



#show()