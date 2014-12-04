from base_handler import *
import logging

class Dashboard(BaseHandler):
    @login_required
    def get(self):
        user = users.get_current_user()
        email = user.email()

        books_owned_by_user = Book.all()
        books_owned_by_user.filter("seller_email =", email)
        books_owned_by_user.order("-date_modified")

        user_has_active_listings = books_owned_by_user.count(1) == 1

        params = {
           'tab_highlight':            1,
           'user':                     user,
           'email':                    email,
           'user_has_active_listings': user_has_active_listings,
           'books_owned_by_user':      books_owned_by_user
        }

        self.renderTemplate('dashboard', params)

    @login_required
    def delete_listing(BaseHandler):
        key = self.request.get('delete_key')
        item = db.get(key)
        db.delete(item)

        if key:
          self.redirect('/dashboard')
