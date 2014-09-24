import webapp2
import os
from google.appengine.ext.webapp import template

class GradeQuiz(webapp2.RequestHandler) :
  def post(self) :
    answer1 = self.request.get('q1')
    answer2 = self.request.get('q2')
    answer3 = self.request.get('q3')
    myHtml = '''
<html>
  <head>
    <link rel="stylesheet" href="css/style.css">
  <script src="scripts/script.js">
  </script>
  </head>
  <body>
    <h1>QUIZ TIME!</h1>
'''

    if (answer1 == 'q1a2') :
      myHtml += 'Question 1 is correct.<br>'
    else :
      myHtml += 'Question 1 is not correct.<br>'

    if (answer2 == 'q2a1') :
      myHtml += 'Question 2 is correct.<br>'
    else :
      myHtml += 'Question 2 is not correct.<br>'

    if (answer3 == 'q3a3') :
      myHtml += 'Question 3 is correct.<br>'
    else :
      myHtml += 'Question 3 is not correct.<br>'

    myHtml += '</body></html>'
    self.response.out.write(myHtml)


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
  </body>
</html>
'''
    self.response.out.write(myHtml)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/submitquiz', GradeQuiz)
], debug=True)

app.run()
