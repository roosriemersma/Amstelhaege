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

    def __init__(self, x, y):
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

    def __init__(self, x, y):
        self.linksBovenX = x
        self.linksBovenY = y

        self.rechtsBovenX = x + self.breedte
        self.rechtsBovenY = y

        self.linksOnderX = x
        self.linksOnderY = y = self.diepte

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

    def __init__(self, x, y):
        self.linksBovenX = x
        self.linksBovenY = y

        self.rechtsBovenX = x + self.breedte
        self.rechtsBovenY = y

        self.linksOnderX = x
        self.linksOnderY = y = self.diepte

        self.rechtsOnderX = x + self.breedte
        self.rechtsOnderY = y + self.diepte

class Water(Woning):
    breedte = 8
    diepte = 10
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
        self.linksOnderY = y = self.diepte

        self.rechtsOnderX = x + self.breedte
        self.rechtsOnderY = y + self.diepte