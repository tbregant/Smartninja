#!/usr/bin/env python
import os
import jinja2
import webapp2


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
        params = {"name": name}
        # params = None
        return self.render_template("omeni.html", params=params)


class RezultatHandler(BaseHandler):
    def post(self):
        vnos = self.request.get("vnos")
        return self.write("Vnesel si: '{}'".format(vnos))


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
        params = {"rezultat": rezultat_izpis, "povratni_url": "/bmicalc"}
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

        params = {"rezultat": rezultat_izpis, "povratni_url": "/kalkulator"}

        return self.render_template("prikazi_rezultat.html", params=params)

        #return self.write("{} {} {} = {}".format(prvo_stevilo, operator_znak , drugo_stevilo, rezultat))

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/omeni', OmeniHandler),
    webapp2.Route('/rezultat', RezultatHandler),
    webapp2.Route('/bmicalc', BmiHandler),
    webapp2.Route('/kalkulator', KalkulatorHandler),
], debug=True)
