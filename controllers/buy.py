from base_handler import *

class Buy(BaseHandler):
  def get(self):
    email = 'unregistered user'
    user = users.get_current_user()

    if user:
      email = user.email()

    books = Book.all()
    q = Book.all()
    q.order("-date_modified")

    search_isbn10 = self.request.get('isbn10')
    search_isbn13 = self.request.get('isbn13')

    search_Author = self.request.get('author2')
    search_Author = search_Author.lower()

    search_title = self.request.get('title2')
    search_title = search_title.lower()

    if search_isbn13:
        q.filter('isbn_13 =', search_isbn10)
    elif search_isbn10:
        q.filter('isbn_10 =', search_isbn13)
    elif search_title and search_Author:
        q.filter('title =', search_title).filter('author =', search_Author)
    elif search_title:
        q.filter('title =', search_title)
    elif search_Author:
        q.filter('author =', search_Author)

    params = { 'tab_highlight': 3,
               'user':          user,
               'email':         email,
               'q' : q,
              'search_title' : search_title,
               'books':         books }

    self.renderTemplate('book_listing', params)
