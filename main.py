import os
import webapp2

app = webapp2.WSGIApplication([
    ('/',          'controllers.landing_page.LandingPage'),
    ('/buy',       'controllers.buy.Buy'),
    ('/dashboard', 'controllers.dashboard.Dashboard'),
    ('/sell',      'controllers.sell.Sell')],
    debug=True)

app.run()
