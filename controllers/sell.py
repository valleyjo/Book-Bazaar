from base_handler import *

class Sell(BaseHandler):
  @login_required
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    params = { 'tab_highlight': 2,
               'user':          user,
               'email':         email }

    self.renderTemplate('sell_book', params)

  def post(self):
    book_params = { 'title':     self.request.get('title'),
                    'author':    self.request.get('author'),
                    'edition':   self.request.get('edition'),
                    'course_id': self.request.get('course_id') }

    new_book = Book.create_book(book_params)
    new_book.put()
    self.redirect('/buy')
