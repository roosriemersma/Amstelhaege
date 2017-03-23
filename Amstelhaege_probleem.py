#160 X 180 meter = 28800 m2
#20% water = 5760 m2
#60% 1sgezins  8x8 = 16m2            2 meter   285000eu   3%
#25% bungalo   10x7.5 = 75m2         3 meter   399000eu   4%
#15% maison    11x10.5 = 115.5m2     6 meter   610000eu   6%
#er zijn 3 opties waar de computer uit moet kiezen:
#20 huizen, 40 huizen of 60 huizen, huizensoort kan verschillen

import random
from random import randint
from tkinter import *
import Woning
import Single
import Bungalo
import Maison

#BELANGRIJKE BRONNEN
#https://www.tutorialspoint.com/python/python_gui_programming.htm

print("Maartje is de shit")

#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
width = 160
height = 180
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)
huizenCoordinaten = []

#def vindCoordinaten(breedte, diepte):
#    coordinatenInvalid = TRUE
#    while coordinatenInvalid:
#        randomX = randint(0, int(160 - breedte))
#        randomY = randint(0, int(180 - diepte))
#        for i in range len(huizenCoordinaten)
#        if randomX >= 0 and randomX <= 10 and randomY >= 0 and randomY <= 10
 #           coordinatenInvalid = FALSE
def vindCoordinaten(breedte, diepte):
    coordinatenInvalid = TRUE
    while coordinatenInvalid:
        randomX = randint(0, int(160 - breedte))
        randomY = randint(0, int(180 - diepte))
        for i in range len(huizenCoordinaten)
            coo = huizenCoordinaten[i]
            if randomX >= coo.x and randomX <= (coo.x+breedte) and randomY >= coo.y and randomY <= (coo.y+diepte):
                coordinatenInvalid = FALSE
    nieuwCoordinaat = [randomX, randomY]
    return nieuwCoordinaat

coordinaten = []

def huizenPlaatsen():
    for j in range(int(Single.Single.aandeelHuizen * maxHuizen)):
        randomX = randint(Single.Single.vrijeruimte, int(width - Single.Single.breedte - Single.Single.vrijeruimte))
        randomY = randint(Single.Single.vrijeruimte, int(height - Single.Single.diepte - Single.Single.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Single.Single.breedte, randomY + Single.Single.diepte, fill="red")
  #      huizenCoordinaten.append(randomX, randomY)
    for k in range(int(Bungalo.Bungalo.percentage * maxHuizen)):
        randomX = randint(Bungalo.Bungalo.vrijeruimte, int(width - Bungalo.Bungalo.breedte - Bungalo.Bungalo.vrijeruimte))
        randomY = randint(Bungalo.Bungalo.vrijeruimte, int(height - Bungalo.Bungalo.diepte - Bungalo.Bungalo.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Bungalo.Bungalo.breedte, randomY + Bungalo.Bungalo.diepte, fill="blue")
   #     huizenCoordinaten.append(randomX, randomY)
    for l in range(int(Maison.Maison.percentage * maxHuizen)):
        randomX = randint(Maison.Maison.vrijeruimte, int(width - Maison.Maison.breedte - Maison.Maison.vrijeruimte))
        randomY = randint(Maison.Maison.vrijeruimte, int(height - Maison.Maison.diepte - Maison.Maison.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Maison.Maison.breedte, randomY + Maison.Maison.diepte, fill="yellow")
    #    huizenCoordinaten.append(randomX, randomY)


def plaatsWoning(Single, Bungalo, Maison):
    for i in range(int(Woning.aand * maxHuizen)):
        randx = randint(0, int(160 - Woning.breedte))76
        randy = randint(0, int(180 - Woning.diepte))
        coordinaatHuis = [randx, randy]
        coordinaten.append(coordinaatHuis)

def huisTekenen(Single, Bungalo, Maison):
    for i in coordinaten:
        huis = coordinaten[i]
        map.create_rectangle(huis[0], huis[1], huis[0] + Woning.breedte, huis[1] + Woning.diepte, fill = Woning.kleur)

#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

huisPlaatsen()

mainloop()
