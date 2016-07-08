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
        if not params:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))


class MainHandler(BaseHandler):
    def get(self):
        return self.render_template("hello.html")

    def post(self):
        # all are white males

        dnk = self.request.get("forensics_input")

        crni_lasje = "CCAGCAATCGC"
        rjavi_lasje = "GCCAGTGCCG"
        korencek_lasje = "TTAGCTATCGC"

        kvadraten_obraz = "GCCACGG"
        okrogel_obraz = "ACCACAA"
        ovalen_obraz = "AGGCCTCA"

        modre_oci = "TTGTGGTGGC"
        zelene_oci = "GGGAGGTGGC"
        rjave_oci = "AAGTAGTGAC"

        def whois(dnk):
            if korencek_lasje in dnk and okrogel_obraz in dnk and rjave_oci in dnk:
                return "Ziga"
            elif crni_lasje in dnk and ovalen_obraz in dnk and modre_oci in dnk:
                return "Matej"
            elif rjavi_lasje in dnk and kvadraten_obraz and zelene_oci in dnk:
                return "Miha"
            else:
                return "Maybe it's an alien from outer space!!@!!"

        dodatni_podatki = dict()

        dodatni_podatki["whois"] = whois(dnk)

        self.write("Entered was: " + dnk + " " + whois(dnk))

        return self.render_template("hello.html", params=dodatni_podatki)

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
