import os
import webapp2
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext.webapp import template

def render_template(handler, templatename, templatevalues) :
    path = os.path.join(os.path.dirname(__file__), 'views/' + templatename)
    html = template.render(path, templatevalues)
    handler.response.out.write(html)

class Book(db.Model):
    title = ndb.StringProperty()
    author = ndb.StringProperty()
    version = ndb.StringProperty()
    course_id = ndb.IntegerProperty()

class LandingPage(webapp2.RequestHandler):
    def get(self):
        email = 'undefined'
        name = 'unregistered user'
        user = users.get_current_user()

        if user:
            email = user.email
            name = user.email

        template_values = {
          'login' : '',
          'logout' : '',
          'email' : email,
          'nickname' : name,
        }

        render_template(self, 'index.html', template_values)

class BookListing(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        books = Book.all()
        template_values = {
            'login' : '',
            'logout' : '',
            'email' : email,
            'nickname' : name,
            'books' : books,
        }

        render_template(self, 'book_listing.html', template_values)

app = webapp2.WSGIApplication([
    ('/', LandingPage),
    ('/books', BookListing),
], debug=True)

app.run()
