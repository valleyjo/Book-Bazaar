import os
import webapp2

app = webapp2.WSGIApplication([
    ('/',                   'controllers.landing_page.LandingPage'),
    ('/buy',                'controllers.buy.Buy'),
    ('/dashboard',          'controllers.dashboard.Dashboard'),
    ('/sell',               'controllers.sell.Sell'),
    ('/delete',             'controllers.delete.Delete'),
    webapp2.Route('/sell_without_isbn', 'controllers.sell.Sell:sell_without_isbn'),
    webapp2.Route('/delete_item', 'controllers.landing_page.LandingPage:delete_item'),
    webapp2.Route('/isbn_search', 'controllers.sell.Sell:find_book_by_isbn')],
    debug=True)

app.run()
