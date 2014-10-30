import os
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template
from models.book import Book

# https://cloud.google.com/appengine/docs/python/tools/webapp/utilmodule
from google.appengine.ext.webapp.util import login_required

class BaseHandler(webapp2.RequestHandler):
  def renderTemplate(self, template_name, params=None) :
    if not params:
      params = {}
    params['login']  = users.create_login_url('/')
    params['logout'] = users.create_logout_url('/')
    path = os.path.join(os.path.dirname(__file__), '../views/' + template_name + '.html')
    html = template.render(path, params)
    self.response.out.write(html)
