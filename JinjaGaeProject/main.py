#!/usr/bin/env python
import os
import jinja2
import webapp2
from models import Sporocilo
from models import Filmi

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)


class BaseHandler(webapp2.RequestHandler):

    def write(self, *a, **kw):
        return self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        return self.write(self.render_str(template, **kw))

    def render_template(self, view_filename, params=None):
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("home.html")


class OmeniHandler(BaseHandler):
    def get(self):
        name = "Bucman"
        # params = {"name": name}
        # params = None
        rezultat = Sporocilo.query().fetch()
        params = {"name": name,
                  "sporocila": rezultat}
        return self.render_template("omeni.html", params=params)


class RezultatHandler(BaseHandler):
    def post(self):
        ime = self.request.get("ime")
        email = self.request.get("email")
        sporocilo = self.request.get("sporocilo")
        sp = Sporocilo(ime=ime, email=email, sporocilo=sporocilo)
        sp.put() # sends to database
        #return self.write("Vnesel si: '{}'".format(vnos))
        rezultat_izpis = "{}, hvala za sporocilo!".format(ime)
        params = {"rezultat": rezultat_izpis,
                  "povratni_url": "/",
                  "heading": "Hvala!"}
        return self.render_template("prikazi_rezultat.html", params=params)


class BmiHandler(BaseHandler):
    def get(self):
        return self.render_template("bmicalc.html")

    def post(self):
        visina = float(self.request.get("visina"))
        teza = float(self.request.get("teza"))
        bmi = teza / (visina**2)
        rezultat_izpis = "<table><tr><td>Visina:</td><td>{}</td></tr>" \
                         "<tr><td>Teza:</td><td>{}</td></tr></table>" \
                         "<br><p>Izracunan BMI indeks je: {}</p>".format(visina, teza, round(bmi,2))
        params = {"rezultat": rezultat_izpis,
                  "povratni_url": "/bmicalc",
                  "heading": "Rezultat"}
        return self.render_template("prikazi_rezultat.html", params=params)

        #return self.write("Tvoja visina je {}, teza: {}. Tvoj BMI indeks je: {}".format(visina, teza, bmi))


class KalkulatorHandler(BaseHandler):
    def get(self):
        return self.render_template("kalkulator.html")

    def post(self):
        rezultat_izpis = ""

        try:
            prvo_stevilo = float(self.request.get("prvo_stevilo"))
            drugo_stevilo = float(self.request.get("drugo_stevilo"))
            operator = str(self.request.get("operator"))
        except ValueError:
            rezultat_izpis = "Vnesel si napacne podatke"

        rezultat = 0
        operator_znak = ""

        try:
            if operator == "plus":
                rezultat = prvo_stevilo + drugo_stevilo
                operator_znak = "+"
            if operator == "minus":
                rezultat = prvo_stevilo - drugo_stevilo
                operator_znak = "-"
            if operator == "krat":
                rezultat = prvo_stevilo * drugo_stevilo
                operator_znak = "*"
            if operator == "deljeno":
                if drugo_stevilo == 0:
                    rezultat_izpis = "Deljenje z 0 ni dovoljeno!"
                else:
                    rezultat = prvo_stevilo / drugo_stevilo
                    operator_znak = '/'
        except UnboundLocalError:
            rezultat_izpis = "Prislo je do napake pri izracunu!"

        if len(rezultat_izpis) == 0:
            rezultat_izpis = "{} {} {} = {}".format(prvo_stevilo, operator_znak , drugo_stevilo, rezultat)

        params = {"rezultat": rezultat_izpis,
                  "povratni_url": "/kalkulator",
                  "heading": "Rezultat"}

        return self.render_template("prikazi_rezultat.html", params=params)

        #return self.write("{} {} {} = {}".format(prvo_stevilo, operator_znak , drugo_stevilo, rezultat))


class ContactHandler(MainHandler):
    def get(self):
        return self.render_template("contact.html")


class SporocilaHandler(MainHandler):
    def get(self):
        sporocila = Sporocilo.query().fetch()
        params = {"sporocila": sporocila}
        return self.render_template("sporocila.html", params=params)


class UrediSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        params = {"sporocilo": sporocilo}
        return self.render_template("uredi_sporocilo.html", params=params)

    def post(self, sporocilo_id):
        nov_vnos = self.request.get("vnos")
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        sporocilo.sporocilo = nov_vnos
        sporocilo.put()
        return self.redirect_to("seznam-sporocil")


class IzbrisiSporociloHandler(BaseHandler):
    def get(self, sporocilo_id):
            sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
            params = {"sporocilo": sporocilo}
            return self.render_template("izbrisi_sporocilo.html", params=params)

    def post(self, sporocilo_id):
        sporocilo = Sporocilo.get_by_id(int(sporocilo_id))
        sporocilo.key.delete()
        return self.redirect_to("seznam-sporocil")


class FilmiHandler(BaseHandler):
    def get(self):
        return self.render_template("vnos_filmov.html")

    def post(self):
        naslov = self.request.get("naslov")
        reziser = self.request.get("reziser")
        glavni_igralec = self.request.get("glavni_igalec")
        zanr = self.request.get("zanr")
        leto_produkcije = int(self.request.get("leto_produkcije"))
        ocena = int(self.request.get("ocena"))
        slika = self.request.get("slika")
        ogledano = int(self.request.get("ogledano"))
        komentar = self.request.get("komentar")

        if ogledano == 1:
            ogledano = True
        else:
            ogledano = False


        film = Filmi(naslov=naslov,
                     reziser=reziser,
                     glavni_igralec=glavni_igralec,
                     zanr=zanr,
                     leto_produkcije=leto_produkcije,
                     ocena=ocena,
                     slika=slika,
                     ogledano=ogledano,
                     komentar=komentar)
        film.put()
        return self.redirect_to("filmi")


class PrikazFilmiHandler(BaseHandler):
    def get(self):
        all_films = Filmi.query().fetch()
        params = {"filmi": all_films}

        return self.render_template("prikaz_filmov.html", params=params)

app = webapp2.WSGIApplication([
    webapp2.Route("/", MainHandler),
    webapp2.Route("/omeni", OmeniHandler),
    webapp2.Route("/rezultat", RezultatHandler),
    webapp2.Route("/bmicalc", BmiHandler),
    webapp2.Route("/kalkulator", KalkulatorHandler),
    webapp2.Route("/contact", ContactHandler),
    webapp2.Route("/sporocila", SporocilaHandler, name="seznam-sporocil"),
    webapp2.Route("/sporocilo/<sporocilo_id:\d+>/uredi", UrediSporociloHandler),
    webapp2.Route("/sporocilo/<sporocilo_id:\d+>/izbrisi", IzbrisiSporociloHandler),
    webapp2.Route("/dodaj_film", FilmiHandler, name="filmi"),
    webapp2.Route("/prikazi_filme", PrikazFilmiHandler),
], debug=True)

