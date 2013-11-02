from pprint import pprint

import webapp2
from paste import httpserver

__author__ = "Brian Tomlinson <darthlukan@gmail.com>"


class Handler(webapp2.RequestHandler):

    def get(self):
        pprint(self.request.GET)
        self.response.write('GET OK')

    def post(self):
        pprint(self.request.POST)
        self.response.write('POST OK')


if __name__ == '__main__':
    app = webapp2.WSGIApplication([
        ('/', Handler),
    ], debug=True)

    httpserver.serve(app, host='127.0.0.1', port='8080')