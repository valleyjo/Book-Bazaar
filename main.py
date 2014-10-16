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
        email = 'unregistered user'
        user = users.get_current_user()

        if user:
            email = user.email()

        template_values = {
            'tab_highlight': 1,
            'user' : user,
            'login' : users.create_login_url('/'),
            'logout' : users.create_logout_url('/'),
            'email' : email,
        }

        render_template(self, 'index.html', template_values)

class Buy(webapp2.RequestHandler):
    def get(self):
        email = 'unregistered user'
        user = users.get_current_user()

        if user:
            email = user.email()

        books = Book.all()

        template_values = {
            'tab_highlight': 3,
            'user': user,
            'login' : users.create_login_url('/'),
            'logout' : users.create_logout_url('/'),
            'email' : email,
            'books' : books,
        }

        render_template(self, 'book_listing.html', template_values)

class Dashboard(webapp2.RequestHandler):
    def get(self):
        email = 'unregistered user'
        user = users.get_current_user()

        if user:
            email = user.email()

        template_values = {
            'tab_highlight': 1,
            'user': user,
            'login' : users.create_login_url('/'),
            'logout' : user.create_logout_url('/'),
            'email' : email,
        }

        render_template(self, 'dashboard.html', template_values)

class Sell(webapp2.RequestHandler):
    def get(self):
        email = 'unregistered user'
        user = users.get_current_user()

        if user:
            email = user.email()

        template_values = {
            'tab_highlight': 2,
            'user': user,
            'login' : users.create_login_url('/'),
            'logout' : users.create_logout_url('/'),
            'email' : email,
        }

        render_template(self, 'add_book.html', template_values)

    def post(self):
        book = Book()
        book.title = self.request.get('title')
        book.author = self.request.get('author')
        book.edition = self.request.get('edition')
        book.course_id = int(self.request.get('course_id'))

        book.put()

        self.redirect('/buy')

app = webapp2.WSGIApplication([
    ('/', LandingPage),
    ('/buy', Buy),
    ('/dashboard', Dashboard),
    ('/sell', Sell),
], debug=True)

app.run()
