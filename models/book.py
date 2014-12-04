import os
import webapp2
from google.appengine.ext import db

class Book(db.Model):
  
  title           = db.StringProperty()
  author          = db.StringProperty()
  edition         = db.StringProperty()
  isbn_10         = db.StringProperty()
  isbn_13         = db.StringProperty()
  picture_url     = db.StringProperty()
  date_modified   = db.DateTimeProperty(auto_now_add=True)
  seller_email    = db.StringProperty() 

  @classmethod
  def create_book(cls, params):
    book = cls()
    book.title       = params['title']
    book.author      = params['author']
    book.edition     = params['edition']
    book.isbn_10     = params['isbn_10']
    book.isbn_13     = params['isbn_13']
    book.picture_url = params['picture_url']
    return book

  def __str__():
      return title + " by " + author
