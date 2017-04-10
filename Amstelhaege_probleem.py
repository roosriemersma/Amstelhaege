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
            if randomX >= (woning.x - breedte - typeWoning.vrijeruimte) and randomX <= (woning.x + woning.breedte + typeWoning.vrijeruimte) and randomY >= (woning.y - diepte - typeWoning.vrijeruimte) and randomY <= (woning.y + woning.diepte + typeWoning.vrijeruimte):
                coordinatenValid = False
    return nieuwCoordinaat

def plaatsWoning(typeWoning):
    nieuwCoordinaat = vindCoordinaten(typeWoning)
    x = nieuwCoordinaat[0]
    y = nieuwCoordinaat[1]
    woning = typeWoning(x, y)
    woningen.append(woning)
    return woning


def tekenWoningen(woningen):
    for woning in woningen:
        map.create_rectangle(woning.x, woning.y, woning.x + woning.breedte , woning.y + woning.diepte , fill = woning.kleur)


for i in range(int(Woning.Single.aandeelHuizen * maxHuizen)):
    plaatsWoning(Woning.Single)
for j in range(int(Woning.Bungalo.aandeelHuizen * maxHuizen)):
    plaatsWoning(Woning.Bungalo)
for k in range(int(Woning.Maison.aandeelHuizen * maxHuizen)):
    plaatsWoning(Woning.Maison)


def tekenWoning(woningen):
    for woning in woningen:
        map.create_rectangle(woning.x, woning.y , woning.x + woning.breedte, woning.y + woning.diepte, fill = woning.kleur)



#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

tekenWoningen(woningen)

mainloop()
