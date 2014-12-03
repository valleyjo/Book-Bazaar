from base_handler import *
import urllib2
import json

class Delete(BaseHandler):
  @login_required
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    params = { 'tab_highlight': 1,
               'user':          user,
               'email':         email }

    self.renderTemplate('index', params)

  def post(self):

    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()
    
   

    self.redirect('/')

  def find_book_by_isbn(self):
    isbn = self.request.get('isbn')
    isbn_param = "ISBN:" + isbn

    url = 'https://openlibrary.org/api/books?bibkeys=ISBN:' + isbn + '&jscmd=data&format=json'
    raw_json = urllib2.urlopen(url).read()
    parsable_json = json.loads(raw_json)

    book_details = {
      'title':       parsable_json[isbn_param]['title'],
      'author':      parsable_json[isbn_param]['authors'][0]['name'],
      'edition':     'Edition Unknown',
      'isbn_10':     parsable_json[isbn_param]['identifiers']['isbn_10'][0],
      'isbn_13':     parsable_json[isbn_param]['identifiers']['isbn_13'][0],
      'picture_url': parsable_json[isbn_param]['cover']['large']
    };

    self.response.headers['Content-Type'] = 'application/json'
    self.response.out.write(json.dumps(book_details))




