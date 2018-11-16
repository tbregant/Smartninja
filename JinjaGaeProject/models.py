from google.appengine.ext import ndb


class Sporocilo(ndb.Model):
    ime = ndb.StringProperty()
    email = ndb.StringProperty()
    sporocilo = ndb.TextProperty()
    datum_vpis = ndb.DateTimeProperty(auto_now_add=True)