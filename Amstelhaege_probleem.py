#BELANGRIJKE BRONNEN
#https://www.tutorialspoint.com/python/python_gui_programming.htm


print("Maartje is de shit")
#160 X 180 meter = 28800 m2
#20% water = 5760 m2
#60% 1sgezins  8x8 = 16m2            2 meter   285000eu   3%
#25% bungalo   10x7.5 = 75m2         3 meter   399000eu   4%
#15% maison    11x10.5 = 115.5m2     6 meter   610000eu   6%
#er zijn 3 opties waar de computer uit moet kiezen:
#20 huizen, 40 huizen of 60 huizen, huizensoort kan verschillen


#soortwoning = {breedte, diepte, waarde, waardevermeerderingPerVrijstaandeMeter}
eengezinswoning = {8, 8, 285000, 0.03}
bungalo = {10, 7.5, 399000, 0.04}
maison = {11, 10.5, 610000, 0.06}


#visualiseren
from tkinter import *

master = Tk()

w = Canvas(master, width=160, height=180)
w.pack()

w.create_line(0, 0, 200, 100)
w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

w.create_rectangle(50, 25, 150, 75, fill="blue")

mainloop()