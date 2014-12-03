from base_handler import *

class Buy(BaseHandler):
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    books = Book.all()

    q = Book.all()

    search_title = self.request.get('title2')

    search_title = search_title.lower()    

    if search_title:
      q.filter("title =", search_title)

    params = { 'tab_highlight': 3,
               'user':          user,
               'email':         email,
               'q' : q,
              'search_title' : search_title,
               'books':         books }

    self.renderTemplate('book_listing', params)
