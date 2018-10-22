

class Stavba(object):

    def __init__(self, st_vrat, st_oken):
        self.st_vrat = st_vrat
        self.st_oken = st_oken

    def show(self):
        print "Stavba = St. vrat: {},\nst_oken: {}\n".format(self.st_vrat, self.st_oken)


class Blok(Stavba):

    def __init__(self, st_vrat, st_oken, st_dvigal):
        # Init metoda nadrejenega objekta se ne izvede samaa, zato je potrebno rocno zagnati init
        # Stavba.__init__(st_vrat, st_oken) # ta nacin je slaba praksa
        super(Blok, self).__init__(st_vrat, st_oken)  # super se nadomesti z objektom iz katerega dedujemo.
        self.st_dvigal = st_dvigal

    def show(self):
        print "Blok = st. vrat: {},\nst_oken: {},\nst_dvigal: {}\n".format(self.st_vrat, self.st_oken, self.st_dvigal)


if __name__ == '__main__':
    stavba = Stavba(1,2)
    stavba.show()

    blok = Blok(80,160,2)
    blok.show()