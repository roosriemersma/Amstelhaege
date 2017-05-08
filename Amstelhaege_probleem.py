#160 X 180 meter = 28800 m2
#20% water = 5760 m2
#60% 1sgezins  8x8 = 16m2            2 meter   285000eu   3%
#25% bungalo   10x7.5 = 75m2         3 meter   399000eu   4%
#15% maison    11x10.5 = 115.5m2     6 meter   610000eu   6%
#er zijn 3 opties waar de computer uit moet kiezen:
#20 huizen, 40 huizen of 60 huizen, huizensoort kan verschilen

import random
from math import sqrt
from random import randint
from tkinter import *
import Woning
import matplotlib.pyplot as plt
import random

#random.seed(3)
#BELANGRIJKE BRONNEN
#https://www.tutorialspoint.com/python/python_gui_programming.htm


#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
vergrotingHuizen = 3

width = 160
height = 180
oppervlakte = width * height
hoeveelHuizen = [20, 40, 60]
maxHuizen = 20   #random.choice(hoeveelHuizen)
woningen = []
besteWoningen = []
waardeKaart = 0
hoogstewaarde = 0


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
        map.create_text(woning.linksBovenX * vergrotingHuizen, woning.linksBovenY * vergrotingHuizen, text= index, font="Times 18 italic")


#HEURISTIEKEN


def conduct():
    for i in range(int(Woning.Single.aandeelHuizen * maxHuizen)):
        plaatsWoning(Woning.Single)
    for j in range(int(Woning.Bungalo.aandeelHuizen * maxHuizen)):
        plaatsWoning(Woning.Bungalo)
    for k in range(int(Woning.Maison.aandeelHuizen * maxHuizen)):
        plaatsWoning(Woning.Maison)

    for woning in woningen:
        index = int(woningen.index(woning))
        shortest_euclidean_distance = 241 * vergrotingHuizen
        for j in range (int(maxHuizen - 1)):
            if j != index:
                if vrijstandTussen(woningen[index], woningen[j]) < shortest_euclidean_distance:
                    shortest_euclidean_distance = vrijstandTussen(woningen[index], woningen[j])
        #print(woning.waarde + woning.waarde * ((shortest_euclidean_distance - woning.vrijeruimte) * woning.waardeStijging))
        global waardeKaart
        waardeKaart = waardeKaart + woning.waarde + woning.waarde * ((shortest_euclidean_distance - woning.vrijeruimte) * woning.waardeStijging)

    #print(waardeKaart)

hoogstewaardes = []
iteraties = []

for i in range(100000):
    conduct()
    print(waardeKaart)
    if waardeKaart > hoogstewaarde:
        hoogstewaarde = waardeKaart
        besteWoningen = woningen
        hoogstewaardes.append(hoogstewaarde)
        iteraties.append(i)
    waardeKaart = 0
    woningen = []

plt.plot(iteraties, hoogstewaardes)
plt.show()

print("De waarde van de beste kaart is ", hoogstewaarde)

#visualiseren
master = Tk()

map = Canvas(master, width=width * vergrotingHuizen, height=height * vergrotingHuizen)
map.pack()

tekenWoningen(besteWoningen)

mainloop()
