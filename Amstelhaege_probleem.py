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
    def __init__(self, breedte, diepte, waarde, waardeStijging, percentage, vrijeruimte):
        self.breedte = breedte
        self.diepte = diepte
        self.waarde = waarde
        self.waardeStijging = waardeStijging
        self.percentage = percentage
        self.vrijeruimte = vrijeruimte

    def __repr__(self):
        return "huis:{}".format(self.breedte)

eengezinswoning = Woning(8, 8, 285000, 0.03, 0.6, 2)
bungalo = Woning(10, 7.5, 399000, 0.04, 0.25, 3)
maison = Woning(11, 10.5, 610000, 0.06, 0.15, 6)

print(eengezinswoning)

#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
width = 160
height = 180
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)

def huizenPlaatsen():
    for j in range(int(eengezinswoning.percentage * maxHuizen)):
        randomX = randint(eengezinswoning.vrijeruimte, int(width - eengezinswoning.breedte - eengezinswoning.vrijeruimte))
        randomY = randint(eengezinswoning.vrijeruimte, int(height - eengezinswoning.diepte - eengezinswoning.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + eengezinswoning.breedte, randomY + eengezinswoning.diepte, fill="red")
    for k in range(int(bungalo.percentage * maxHuizen)):
        randomX = randint(bungalo.vrijeruimte, int(width - bungalo.breedte - bungalo.vrijeruimte))
        randomY = randint(bungalo.vrijeruimte, int(height - bungalo.diepte - bungalo.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + bungalo.breedte, randomY + bungalo.diepte, fill="green")
    for l in range(int(maison.percentage * maxHuizen)):
        randomX = randint(maison.vrijeruimte, int(width - maison.breedte - maison.vrijeruimte))
        randomY = randint(maison.vrijeruimte, int(height - maison.diepte - maison.vrijeruimte))
        map.create_rectangle(randomX, randomY, randomX + maison.breedte, randomY + maison.diepte, fill="yellow")


#def huizenPlaatsen2()
#    for i in range(int())


#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

huizenPlaatsen()

mainloop()
