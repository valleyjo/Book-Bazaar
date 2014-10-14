import os
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues) :
  path = os.path.join(os.path.dirname(__file__), 'templates/' + templatename)
  html = template.render(path, templatevalues)
  handler.response.out.write(html)

class LandingPage(webapp2.RequestHandler) :
  def get(self) :
    self.response.out.write(myHtml)

app = webapp2.WSGIApplication([
    ('/', LandingPage),
], debug=True)

app.run()
