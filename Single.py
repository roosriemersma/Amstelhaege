class Single(Woning):
    breedte = 8
    diepte = 8
    waarde = 285000
    waardeStijging = 0.03
    aandeelHuizen = 0.6
    kleur = "red"
    vrijeruimte = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y