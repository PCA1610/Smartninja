import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Hello!')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
