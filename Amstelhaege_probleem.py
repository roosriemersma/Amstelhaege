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

#BELANGRIJKE BRONNEN
#https://www.tutorialspoint.com/python/python_gui_programming.htm

print("Maartje is de shit")

class Woning(object):
    #def __init__(self, breedte, diepte, waarde, waardeStijging, percentage):
    #    self.breedte = breedte
    #    self.diepte = diepte
    #    self.waarde = waarde
    #    self.waardeStijging = waardeStijging
    #    self.percentage = percentage
    #    self.kleur = kleur

    def __repr__(self):
        return "huis:{}".format(self.breedte)

class Maison(Woning):
    breedte = 11
    diepte = 10.5
    waarde = 1
    waardeStijging = 1
    percentage = 0.1
    kleur = "rood"

    def __init__(self, x, y):
        self.x = x
        self.y = y

Maison.waarde
maison = Maison(3,5)
maison.x
eengezinswoning = Woning(8, 8, 285000, 0.03, 0.6, "red")
bungalo = Woning(10, 7.5, 399000, 0.04, 0.25, "green")
maison = Woning(11, 10.5, 610000, 0.06, 0.15, "yellow")

print(eengezinswoning)

#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
width = 160
height = 180
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)
huizenCoordinaten = []

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
    for j in range(int(eengezinswoning.percentage * maxHuizen)):
            randomX = randint(0, int(160 - eengezinswoning.breedte))
            randomY = randint(0, int(180 - eengezinswoning.diepte))
        map.create_rectangle(randomX, randomY, randomX + eengezinswoning.breedte, randomY + eengezinswoning.diepte, fill="red")
        huizenCoordinaten.append(randomX, randomY)
    for k in range(int(bungalo.percentage * maxHuizen)):
        randomX = randint(0, int(160 - bungalo.breedte))
        randomY = randint(0, int(180 - bungalo.diepte))
        map.create_rectangle(randomX, randomY, randomX + bungalo.breedte, randomY + bungalo.diepte, fill="blue")
        huizenCoordinaten.append(randomX, randomY)
    for l in range(int(maison.percentage * maxHuizen)):
        randomX = randint(0, int(160 - maison.breedte))
        randomY = randint(0, int(180 - maison.diepte))
        map.create_rectangle(randomX, randomY, randomX + maison.breedte, randomY + maison.diepte, fill="yellow")
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

#def huizenPlaatsen2()
#    for i in range(int())
#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

huisPlaatsen()

mainloop()
