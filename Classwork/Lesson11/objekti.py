
class MojPrviClass(object):

    def __init__(self, ime): # inicializacijska metoda, se izvede ko iz classa naredimo objekt
        self.ime = ime
        print "pozdrav iz __init_ - {}".format(ime)

    def pozdravi(self):
        print "Pozdravljen {}".format(self.ime)

mojclass = MojPrviClass("TOmaz")
mojclass.pozdravi()

print mojclass.ime