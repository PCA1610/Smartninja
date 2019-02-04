#!/usr/bin/env python
import os
import random

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


class Capital:
    def __init__(self, capital, country, image):
        self.capital = capital
        self.country = country
        self.image = image


def setup_data():
    lj = Capital(capital="Ljubljana", country="Slovenia", image="/assets/img/city1.jpg")
    zg = Capital(capital="Zagreb", country="Croatia", image="/assets/img/city2.jpg")
    w = Capital(capital="Vienna", country="Austria", image="/assets/img/city3.jpg")
    rm = Capital(capital="Rome", country="Italy", image="/assets/img/city4.jpg")
    be = Capital(capital="Berlin", country="Germany", image="/assets/img/city5.jpg")

    return [lj, zg, w, rm, be]


class MainHandler(BaseHandler):
    def get(self):

        city_list = {"Austria": "Vienna", "Germany": "Berlin", "Italy": "Rome"}
        city = city_list[random.randint(0, 2)]

        return self.render_template("index.html", params={"random_city": city})

    def post(self):
        result = self.request.get("city")

        if result == "Vienna":
            return self.render_template("index.html", params={"result": result})
        else:
            guess = "Sorry, but your guess is to low. Try a bit higher."

            return self.render_template("index.html", params={"result": guess})


class AboutHandler(BaseHandler):
    def get(self):
        return self.render_template("about.html")


class ResultHandler(BaseHandler):
    def get(self):
        return self.render_template("result.html")


class ContactHandler(BaseHandler):
    def get(self):
        return self.render_template("contact.html")


class ProjectsHandler(BaseHandler):
    def get(self):
        return  self.render_template("projects.html")


class BlogHandler(BaseHandler):
    def get(self):
        return self.render_template("blog.html")




app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/about', AboutHandler),
    webapp2.Route('/result', ResultHandler),
    webapp2.Route('/contact', ContactHandler),
    webapp2.Route('/projects', ProjectsHandler),
    webapp2.Route('/blog', BlogHandler),
], debug=True)


# run on localhost server
gae_env = False  # False: non-GAE localhost server; True: GAE on either localhost or on Google Cloud
if not gae_env:
    def main():
        from paste import httpserver
        from paste.cascade import Cascade
        from paste.urlparser import StaticURLParser

        assets_dir = os.path.join(os.path.dirname(__file__))
        static_app = StaticURLParser(directory=assets_dir)

        web_app = Cascade([app, static_app])
        httpserver.serve(web_app, host='localhost', port='8000')


    if __name__ == '__main__':
        main()
