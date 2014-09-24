import webapp2
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler) :
  def get(self) :
    myHtml = '''
<html>
  <head>
    <link rel="stylesheet" href="css/style.css">
  <script src="scripts/script.js">
  </script>
  </head>
  <body>
    <h1>CS1520 Group 8</h1>
    <p>This is a test of the Github push to deploy feature</p>
  </body>
</html>
'''
    self.response.out.write(myHtml)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

app.run()
