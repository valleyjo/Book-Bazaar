import webapp2
import os
from google.appengine.ext.webapp import template

class MainPage(webapp2.RequestHandler) :
  def get(self) :
    myHtml = '''
<html>
  <head>

    <!-- Styles -->
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet"
    href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">

    <!-- JS -->
    <script
        src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js">
    </script>
    <script
        src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js">
    </script>
    <script
        src="scripts/script.js">
    </script>

  </head>
  <body>
  </body>
  <div class="container">
    <div class="header">
      <ul class="nav nav-pills pull-right">
        <li class="active"><a href="#">Home</a></li>
        <li><a href="#">About</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
      <h3 class="text-muted">Book Bazaar</h3>
    </div>

    <div class="jumbotron">
      <h1>Book Bazaar</h1>
      <p class="lead">No hassle book re-sale to other students at your university</p>
      <p><a id="sign-up-button" class="btn btn-lg btn-success" href="#" role="button">Sign up today</a></p>
    </div>

    <div class="row marketing">
      <div class="col-lg-6">
        <h4>No middleman</h4>
        <p>We don't take any part of your sale price. We simply help you find someone who wants to buy your books and negotiate a price.</p>

        <h4>Subheading</h4>
        <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

        <h4>Subheading</h4>
        <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
      </div>

      <div class="col-lg-6">
        <h4>Subheading</h4>
        <p>Donec id elit non mi porta gravida at eget metus. Maecenas faucibus mollis interdum.</p>

        <h4>Subheading</h4>
        <p>Morbi leo risus, porta ac consectetur ac, vestibulum at eros. Cras mattis consectetur purus sit amet fermentum.</p>

        <h4>Subheading</h4>
        <p>Maecenas sed diam eget risus varius blandit sit amet non magna.</p>
      </div>
    </div>

    <div class="footer">
      <p>&copy; Company 2014</p>
    </div>
  </div> <!-- /container -->                                                                                                                                                                                                                                                                                   </div> <!-- /container -->
</html>
'''
    self.response.out.write(myHtml)

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

app.run()
