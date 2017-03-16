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

#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter, precentage huizen, kleur}
eengezinswoning = [8, 8, 285000, 0.03, 0.6, "red"]
bungalo = [10, 7.5, 399000, 0.04, 0.25, "blue"]
maison = [11, 10.5, 610000, 0.06, 0.15, "yellow"]
width = 160
height = 180
hoeveelHuizen = [20, 40, 60]
maxHuizen = random.choice(hoeveelHuizen)

def huizenPlaatsen():
    for j in range(int(0.6 * maxHuizen)):
        randomX = randint(0, 160)
        randomY = randint(0, 180)
        map.create_rectangle(randomX, randomY, randomX + eengezinswoning[0], randomY + eengezinswoning[1], fill="red")
    for k in range(int(0.25 * maxHuizen)):
        randomX = randint(0, 160)
        randomY = randint(0, 180)
        map.create_rectangle(randomX, randomY, randomX + bungalo[0], randomY + bungalo[1], fill="blue")
    for l in range(int(0.15 * maxHuizen)):
        randomX = randint(0, 160)
        randomY = randint(0, 180)
        map.create_rectangle(randomX, randomY, randomX + maison[0], randomY + maison[1], fill="yellow")

#visualiseren
master = Tk()

map = Canvas(master, width=width, height=height)
map.pack()

huizenPlaatsen()

mainloop()
