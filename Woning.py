import random
from math import sqrt
import random
class Woning(object):

    #def RuimteTussenWoningen:
        # Berekend de vrije ruimte

    def __repr__(self):
        return "huis:{}".format(self.breedte)

class Single(Woning):
    breedte = 8
    diepte = 8
    waarde = 285000
    waardeStijging = 0.03
    aandeelHuizen = 0.6
    kleur = "red"
    vrijeruimte = 2
    kortsteAfstand = 0

    def __init__(self, x, y):
        self.type = "Single"

        self.linksBovenX = x
        self.linksBovenY = y

        self.rechtsBovenX = x + self.breedte
        self.rechtsBovenY = y

        self.linksOnderX = x
        self.linksOnderY = y + self.diepte

        self.rechtsOnderX = x + self.breedte
        self.rechtsOnderY = y + self.diepte


class Bungalo(Woning):
    breedte = 10
    diepte = 7.5
    waarde = 399000
    waardeStijging = 0.04
    aandeelHuizen = 0.25
    kleur = "yellow"
    vrijeruimte = 3
    kortsteAfstand = 0

    def __init__(self, x, y):
        self.type = "Bungalo"

        self.linksBovenX = x
        self.linksBovenY = y

        self.rechtsBovenX = x + self.breedte
        self.rechtsBovenY = y

        self.linksOnderX = x
        self.linksOnderY = y + self.diepte

        self.rechtsOnderX = x + self.breedte
        self.rechtsOnderY = y + self.diepte

class Maison(Woning):
    breedte = 11
    diepte = 10.5
    waarde = 610000
    waardeStijging = 0.06
    aandeelHuizen = 0.15
    kleur = "green2"
    vrijeruimte = 6
    kortsteAfstand = 0

    def __init__(self, x, y):
        self.type = "Maison"

        self.linksBovenX = x
        self.linksBovenY = y

        self.rechtsBovenX = x + self.breedte
        self.rechtsBovenY = y

        self.linksOnderX = x
        self.linksOnderY = y + self.diepte

        self.rechtsOnderX = x + self.breedte
        self.rechtsOnderY = y + self.diepte


class Water(Woning):
    watereenheden = [1,2,3,4]
    aantalWatereenheden = 2  #random.choice(watereenheden)


    if aantalWatereenheden == 1:
        breedte = random.randint(38, 152)
        diepte = 5760 / breedte
        """
    elif aantalWatereenheden == 2:
        oppervlakte1 = 5760 / random.randint(1,5760)
        vierkantzijden1 = int(sqrt(oppervlakte1))
        breedte1 = random.randint(vierkantzijden1/2, vierkantzijden1*2)
        diepte1 = oppervlakte1 / breedte1

        oppervlakte2 = 5760 - oppervlakte1
        vierkantzijden2 = int(sqrt(oppervlakte2))
        breedte2 = random.randint(vierkantzijden2 / 2, vierkantzijden2 * 2)
        diepte2 = oppervlakte2 / breedte2

    elif aantalWatereenheden == 3:
        oppervlakte1 = 5760 / random.randint(1, 5760)
        vierkantzijden1 = int(sqrt(oppervlakte1))
        breedte1 = random.randint(vierkantzijden1 / 2, vierkantzijden1 * 2)
        diepte1 = oppervlakte1 / breedte1

        oppervlakte2 = (5760 - oppervlakte1) / random.randint(1, (5760 - oppervlakte1))
        vierkantzijden2 = int(sqrt(oppervlakte2))
        breedte2 = random.randint(vierkantzijden2 / 2, vierkantzijden2 * 2)
        diepte2 = oppervlakte2 / breedte2

        oppervlakte3 = 5760 - oppervlakte1 - oppervlakte2
        vierkantzijden3 = int(sqrt(oppervlakte3))
        breedte3 = random.randint(vierkantzijden3 / 2, vierkantzijden3 * 2)
        diepte3 = oppervlakte3 / breedte3

    elif aantalWatereenheden == 4:
        oppervlakte1 = 5760 / random.randint(1, 5760)
        vierkantzijden1 = int(sqrt(oppervlakte1))
        breedte1 = random.randint(vierkantzijden1 / 2, vierkantzijden1 * 2)
        diepte1 = oppervlakte1 / breedte1

        oppervlakte2 = (5760 - oppervlakte1) / random.randint(1, (5760 - oppervlakte1))
        vierkantzijden2 = int(sqrt(oppervlakte2))
        breedte2 = random.randint(vierkantzijden2 / 2, vierkantzijden2 * 2)
        diepte2 = oppervlakte2 / breedte2

        oppervlakte3 = (5760 - oppervlakte1 - oppervlakte2) / random.randint((5760 - oppervlakte1 - oppervlakte2))
        vierkantzijden4 = int(sqrt(oppervlakte4))
        breedte4 = random.randint(vierkantzijden4 / 2, vierkantzijden4 * 2)
        diepte4 = oppervlakte

        oppervlakte4 = 5760 - oppervlakte1 - oppervlakte2 - oppervlakte3
        vierkantzijden4 = int(sqrt(oppervlakte4))
        breedte4 = random.randint(vierkantzijden4 / 2, vierkantzijden4 * 2)
        diepte4 = oppervlakte4 / breedte4
        """
    elif aantalWatereenheden == 2:
        breedte = random.randint(27, 107)
        diepte = 2880/ breedte
    elif aantalWatereenheden == 3:
        breedte = random.randint(22, 87)
        diepte = 1920 / breedte
    elif aantalWatereenheden == 4:
        breedte = random.randint(19, 76)
        diepte = 1440 / breedte
''''''
    waarde = 0
    waardeStijging = 0
    aandeelHuizen = 0
    kleur = "blue"
    vrijeruimte = 0

    def __init__(self, x, y):
        self.linksBovenX = x
        self.linksBovenY = y

        self.rechtsBovenX = x + self.breedte
        self.rechtsBovenY = y

        self.linksOnderX = x
        self.linksOnderY = y + self.diepte

        self.rechtsOnderX = x + self.breedte
        self.rechtsOnderY = y + self.diepte