from google.appengine.ext import ndb


class Sporocilo(ndb.Model):
    ime = ndb.StringProperty()
    email = ndb.StringProperty()
    sporocilo = ndb.TextProperty()
    datum_vpis = ndb.DateTimeProperty(auto_now_add=True)


class Filmi(ndb.Model):
    naslov = ndb.StringProperty(required=True)
    reziser = ndb.StringProperty()
    glavni_igralec = ndb.StringProperty()
    zanr = ndb.StringProperty()
    leto_produkcije = ndb.IntegerProperty()
    ocena = ndb.IntegerProperty()
    slika = ndb.StringProperty(required=True)
    ogledano = ndb.BooleanProperty(required=True)
    datum_vnosa = ndb.DateTimeProperty(auto_now_add=True)
    komentar = ndb.TextProperty()