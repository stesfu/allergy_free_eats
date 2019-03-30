#-*- coding:utf-8 -*-

import webapp2
import jinja2
import os

jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = jinja_current_directory.get_template("templates/homePage.html")
        self.response.write(welcome_template.render())

app = webapp2.WSGIApplication([('/', WelcomeHandler),], debug=True)
