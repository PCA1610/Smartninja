#!/usr/bin/env python
import os

import jinja2
import webapp2
from pymongo import MongoClient
from bson import ObjectId


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


class Person(object):
    def __init__(self, person_id, name, food):
        self.person_id = person_id
        self.name = name
        self.food = food


class MainHandler(BaseHandler):
    def get_person_list(self):
        person_list = []

        client = MongoClient()
        db = client.test_database
        people = db.people

        for p in people.find():
            person_list.append(Person(p['_id'], p['name'], p['food']))

        return person_list

    def get(self):
        return self.render_template("index.html", params={"persons": self.get_person_list()})


class ProfilHandler(BaseHandler):
    def get(self, person_id):
        client = MongoClient()
        db = client.test_database
        people = db.people

        person = people.find_one({"_id": ObjectId(person_id)})
        return self.render_template("profil.html", params={"name": person['name'], "food": person['food']})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    webapp2.Route('/profil/<person_id:>', ProfilHandler),
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
