#160 X 180 meter = 28800 m2
#20% water = 5760 m2
#60% 1sgezins  8x8 = 16m2            2 meter   285000eu   3%
#25% bungalo   10x7.5 = 75m2         3 meter   399000eu   4%
#15% maison    11x10.5 = 115.5m2     6 meter   610000eu   6%
#er zijn 3 opties waar de computer uit moet kiezen:
#20 huizen, 40 huizen of 60 huizen, huizensoort kan verschillen

import random
from math import sqrt
from random import randint
from tkinter import *
import Woning
import random

random.seed(4)
#BELANGRIJKE BRONNEN
#https://www.tutorialspoint.com/python/python_gui_programming.htm


#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
width = 160 * 3
height = 180 * 3
oppervlakte = width * height
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)
woningen = []


def vindCoordinaten(typeWoning):
    breedte = typeWoning.breedte
    diepte = typeWoning.diepte
    coordinatenValid = False
    nieuwCoordinaat = []
    while not coordinatenValid:
        coordinatenValid = True
        randomX = randint(typeWoning.vrijeruimte, int(width - breedte))
        randomY = randint(typeWoning.vrijeruimte, int(height - diepte))
        nieuwCoordinaat = [randomX, randomY]
        for woning in woningen:
            if randomX >= (woning.linksBovenX - breedte - typeWoning.vrijeruimte) and randomX <= (woning.linksBovenX + woning.breedte + typeWoning.vrijeruimte) and randomY >= (woning.linksBovenY - diepte - typeWoning.vrijeruimte) and randomY <= (woning.linksBovenY + woning.diepte + typeWoning.vrijeruimte):
                coordinatenValid = False
    return nieuwCoordinaat


def vrijstandTussen(woningA, woningB):
    x1 = woningA.linksBovenX
    y1 = woningA.linksBovenY
    x1b = woningA.rechtsOnderX
    y1b = woningA.rechtsOnderY

    x2 = woningB.linksBovenX
    y2 = woningB.linksBovenY
    x2b = woningB.rechtsOnderX
    y2b = woningB.rechtsOnderY

    left = x2b < x1
    right = x1b < x2
    bottom = y2b < y2
    top = y1b < y2
    if top and left:
        euclidean_distance = sqrt((x1 - x2b) ** 2 + (y1b - y2) ** 2)
        print("euclidean_distance = ", euclidean_distance)
        return euclidean_distance
    elif left and bottom:
        euclidean_distance = sqrt((x1 - x2b) ** 2 + (y1 - y2b) ** 2)
        print(euclidean_distance)
        return euclidean_distance
    elif bottom and right:
        euclidean_distance = sqrt((x1b - x2) ** 2 + (y1 - y2b) ** 2)
        print(euclidean_distance)
        return euclidean_distance
    elif right and top:
        euclidean_distance = sqrt((x1b - x2) ** 2 + (y1b - y2) ** 2)
        print(euclidean_distance)
        return euclidean_distance
    elif left:
        print(x1 - x2b)
        return x1 - x2b
    elif right:
        print(x2 - x1b)
        return x2 - x1b
    elif bottom:
        print(y1 - y2b)
        return y1 - y2b
    elif top:
        print(y2 - y1b)
        return y2 - y1b

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
        map.create_rectangle(woning.linksBovenX, woning.linksBovenY, woning.linksBovenX + woning.breedte , woning.linksBovenY + woning.diepte , fill = woning.kleur)
        map.create_text(woning.linksBovenX, woning.linksBovenY, text= index, font="Times 18 italic")

#def berekenVrijstand (huisA, huisB):
#    en dan zeggen we dus a nee oke bor. wat ik een beetje mee zit te struggelen nu. waarom is roos weg eigenlijk
#    tussen twee huizen de afstand kunnen berekenen is eerste zorg
#    later gaan we zorgen met een geneste for loop dat elke woning de afstand tot elke woning controleert.

for i in range(int(Woning.Single.aandeelHuizen * maxHuizen)):
    plaatsWoning(Woning.Single)
for j in range(int(Woning.Bungalo.aandeelHuizen * maxHuizen)):
    plaatsWoning(Woning.Bungalo)
for k in range(int(Woning.Maison.aandeelHuizen * maxHuizen)):
    plaatsWoning(Woning.Maison)

vrijstandTussen(woningen[3], woningen[0])

#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

tekenWoningen(woningen)

mainloop()
