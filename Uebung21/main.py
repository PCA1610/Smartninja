#!/usr/bin/env python
import os

import jinja2
import webapp2
from pymongo import MongoClient

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
        todo_list = ["Netflix", "Training", "Python"]

        return self.render_template("index.html", params={"todo_list": todo_list})

    def post(self):

        all_tasks = task.finde()
        tasks = self.request.get("task")
        self.writ_to_db(tasks)

        return self.render_template("index.html", params={"test": all_tasks})

    def db_handler(selfs):
        client = MongoClient()

        db = client.todo_list

        tasks = db.tasks

    def writ_to_db(self, new_task):
        client = MongoClient()

        db = client.todo_list

        tasks = db.tasks

        tasks.insert({"Task": new_task})


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
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
