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

#BELANGRIJKE BRONNEN
#https://www.tutorialspoint.com/python/python_gui_programming.htm


#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
width = 160
height = 180
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)
woningen = []

def vindCoordinaten(typeWoning):
    breedte = typeWoning.breedte
    diepte = typeWoning.diepte
    coordinatenValid = FALSE
    nieuwCoordinaat = []
    while not coordinatenValid:
        coordinatenValid = TRUE
        randomX = randint(0, int(160 - breedte))
        randomY = randint(0, int(180 - diepte))
        for woning in woningen:
            if randomX >= woning.x and randomX <= (woning.x+breedte) and randomY >= woning.y and randomY <= (woning.y+diepte):
                coordinatenValid = FALSE
        nieuwCoordinaat = [randomX, randomY]
    return nieuwCoordinaat


def huizenPlaatsen():
    for j in range(int(Woning.Single.aandeelHuizen * maxHuizen)):
        randomX = randint(Woning.Single.vrijeruimte, int(width - Woning.Single.breedte - Woning.Single.vrijeruimte))
        randomY = randint(Woning.Single.vrijeruimte, int(height - Woning.Single.diepte - Woning.Single.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Woning.Single.breedte, randomY + Woning.Single.diepte, fill="red")
  #      huizenCoordinaten.append(randomX, randomY)
    for k in range(int(Woning.Bungalo.aandeelHuizen * maxHuizen)):
        randomX = randint(Woning.Bungalo.vrijeruimte, int(width - Woning.Bungalo.breedte - Woning.Bungalo.vrijeruimte))
        randomY = randint(Woning.Bungalo.vrijeruimte, int(height - Woning.Bungalo.diepte - Woning.Bungalo.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Woning.Bungalo.breedte, randomY + Woning.Bungalo.diepte, fill="blue")
   #     huizenCoordinaten.append(randomX, randomY)
    for l in range(int(Woning.Maison.aandeelHuizen * maxHuizen)):
        randomX = randint(Woning.Maison.vrijeruimte, int(width - Woning.Maison.breedte - Woning.Maison.vrijeruimte))
        randomY = randint(Woning.Maison.vrijeruimte, int(height - Woning.Maison.diepte - Woning.Maison.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + Woning.Maison.breedte, randomY + Woning.Maison.diepte, fill="yellow")
    #    huizenCoordinaten.append(randomX, randomY)


def plaatsWoning(typeWoning):
    x = nieuwCoordinaat[0]
    y = nieuwCoordinaat[1]
    woning = typeWoning(x, y)
    for i in range(int(Woning.aandeelHuizen * maxHuizen)):
        randx = randint(0, int(160 - Woning.breedte))#76
        randy = randint(0, int(180 - Woning.diepte))
        coordinaatHuis = [randx, randy]
        coordinaten.append(coordinaatHuis)
    return woning


def tekenWoning(Single, Bungalo, Maison):
    for woning in woningen:
        map.create_rectangle(woning.x, woning.y , woning.x + woning.breedte, woning.y + woning.diepte, fill = woning.kleur)

#def huizenPlaatsen2()
#    for i in range(int())
#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

huizenPlaatsen()

mainloop()
