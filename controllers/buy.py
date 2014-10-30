from base_handler import *

class Buy(BaseHandler):
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    books = Book.all()

    params = { 'tab_highlight': 3,
               'user':          user,
               'email':         email,
               'books':         books }

    self.renderTemplate('book_listing', params)
