import os
import webapp2

app = webapp2.WSGIApplication([
    ('/',            'controllers.landing_page.LandingPage'),
    ('/buy',         'controllers.buy.Buy'),
    ('/dashboard',   'controllers.dashboard.Dashboard'),
    ('/sell',        'controllers.sell.Sell'),
    ('/sell2',        'controllers.sell2.Sell'),
    ('/delete',        'controllers.delete.Delete'),
    webapp2.Route('/isbn_search', 'controllers.sell.Sell:find_book_by_isbn')],
    debug=True)

app.run()
