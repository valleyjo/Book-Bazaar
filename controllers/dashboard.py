from base_handler import *

class Dashboard(BaseHandler):
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    params = { 'tab_highlight': 1,
               'user': user,
               'email' : email }

    self.renderTemplate('dashboard', params)
