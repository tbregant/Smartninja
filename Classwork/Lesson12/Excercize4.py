from math import pi
# ploscina in obseg kroga


class Krog(object):

    def __init__(self, polmer):
        self.polmer = polmer

    def izracunaj_obseg(self):
        return 2 * pi * self.polmer

    def izracunaj_ploscino(self):
        return pi * self.polmer ** 2


krog = Krog(4.5)

ploscina = krog.izracunaj_ploscino()
obseg = krog.izracunaj_obseg()

print ploscina
print obseg