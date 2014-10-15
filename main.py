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
    title = db.StringProperty()
    author = db.StringProperty()
    edition = db.StringProperty()
    course_id = db.IntegerProperty()
    last_modified_date = db.DateTimeProperty(auto_now_add=True)

class LandingPage(webapp2.RequestHandler):
    def get(self):
        email = ''
        name = ''
        logout_url = ''
        user = users.get_current_user()

        if user:
            email = user.email()
            name = user.nickname()
            logout_url = users.create_logout_url('/')

        template_values = {
            'login' : users.create_login_url('/'),
            'logout' : logout_url,
            'email' : email,
            'nickname' : name,
        }

        render_template(self, 'index.html', template_values)

class BookListing(webapp2.RequestHandler):
    def get(self):
        email = ''
        name = ''
        user = users.get_current_user()

        if user:
            email = user.email()
            name = user.nickname()

        books = Book.all()

        template_values = {
            'login' : users.create_login_url('/'),
            'logout' : users.create_logout_url('/'),
            'email' : email,
            'nickname' : nickname,
            'books' : books,
        }

        render_template(self, 'book_listing.html', template_values)

class Dashboard(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            email = user.email()
            name = user.nickname()

        template_values = {
            'login' : users.create_login_url('/'),
            'logout' : users.create_logout_url('/'),
            'email' : email,
            'nickname' : name,
        }

        render_template(self, 'dashboard.html', template_values)

app = webapp2.WSGIApplication([
    ('/', LandingPage),
    ('/books', BookListing),
    ('/dashboard', Dashboard),
], debug=True)

app.run()
