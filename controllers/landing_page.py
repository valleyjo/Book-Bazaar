from base_handler import *
import logging

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

  def post(self):


    key = self.request.get('k')
    item = db.get(key)
    db.delete(item)



    if key:

      self.redirect('/buy')
   

