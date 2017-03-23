class Maison(Woning):
    breedte = 11
    diepte = 10.5
    waarde = 610000
    waardeStijging = 0.06
    aandeelHuizen = 0.15
    kleur = "yellow"
    vrijeruimte = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y