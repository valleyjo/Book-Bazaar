from base_handler import *

class LandingPage(BaseHandler):
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    books = Book.all()

    q = Book.all()

    q.filter("seller_email =", email)

    q.order("-date_modified")

    params = { 'tab_highlight': 1,
               'user':          user,
               'email':         email,
               'q' : q,
               'books':         books }

    self.renderTemplate('index', params)


