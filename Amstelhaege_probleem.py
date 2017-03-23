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

print("Maaartje is de shit")

#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
width = 160
height = 180
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)
woningen = []

def vindCoordinaten(breedte, diepte):
    coordinatenInvalid = TRUE
    while coordinatenInvalid:
        randomX = randint(0, int(160 - breedte))
        randomY = randint(0, int(180 - diepte))
        for woning in woningen
            if randomX >= woning.x and randomX <= (woning.x+breedte) and randomY >= woning.y and randomY <= (woning.y+diepte):
                coordinatenInvalid = FALSE
    nieuwCoordinaat = [randomX, randomY]
    return nieuwCoordinaat


def huizenPlaatsen():
    for j in range(int(eengezinswoning.percentage * maxHuizen)):
        randomX = randint(Single.vrijeruimte, int(width - Single.breedte - Single.vrijeruimte))
        randomY = randint(Single.vrijeruimte, int(height - Single.diepte - Single.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Single.breedte, randomY + Single.diepte, fill="red")
        huizenCoordinaten.append(randomX, randomY)
    for k in range(int(Bungalo.percentage * maxHuizen)):
        randomX = randint(Bungalo.vrijeruimte, int(width - Bungalo.breedte - Bungalo.vrijeruimte))
        randomY = randint(Bungalo.vrijeruimte, int(height - Bungalo.diepte - Bungalo.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Bungalo.breedte, randomY + Bungalo.diepte, fill="blue")
        huizenCoordinaten.append(randomX, randomY)
    for l in range(int(Maison.percentage * maxHuizen)):
        randomX = randint(Maison.vrijeruimte, int(width - Maison.breedte - Maison.vrijeruimte))
        randomY = randint(Maison.vrijeruimte, int(height - Maison.diepte - Maison.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Maison.breedte, randomY + Maison.diepte, fill="yellow")
        huizenCoordinaten.append(randomX, randomY)


def huizenLeuk(Woning):
    for i in range(int(Woning.percentage * maxHuizen)):
        randx = randint(0, int(160 - Woning.breedte))76
        randy = randint(0, int(180 - Woning.diepte))
        coordinaatHuis = [randx, randy]
        coordinaten.append(coordinaatHuis)

def huisTekenen(Woning):
    for i in coordinaten:
        huis = coordinaten[i]
        map.create_rectangle(huis[0], huis[1], huis[0] + Woning.breedte, huis[1] + Woning.diepte, fill = Woning.kleur)

#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

huisPlaatsen()

mainloop()
