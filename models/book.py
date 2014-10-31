import os
import webapp2
from google.appengine.ext import db

class Book(db.Model):
  title         = db.StringProperty()
  author        = db.StringProperty()
  edition       = db.StringProperty()
  isbn_10       = db.IntegerProperty()
  isbn_13       = db.IntegerProperty()
  course_id     = db.StringProperty()
  date_modified = db.DateTimeProperty(auto_now_add=True)

  @classmethod
  def create_book(cls, params):
    book = cls()
    book.title     = params['title']
    book.author    = params['author']
    book.edition   = params['edition']
    book.course_id = params['course_id']
    return book

  def __str__():
      return title + " by " + author
