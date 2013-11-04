import webapp2
from paste import httpserver

__author__ = "Brian Tomlinson <darthlukan@gmail.com>"


class Processor(object):
    """
    Performs some basic validation of data and cleanup as needed
    before passing off to the "heavy lifter"

    NOTE: Dummy logic for now as placeholders.
    """
    def __init__(self):
        pass

    def validate(self, params):
        """
        Do we even have valid data to work with?
        """
        if params:
            return "validated: %s" % params
        return False

    def clean(self, params):
        """
        Clean it up prior to sending to the processor
        """
        if params:
            return "cleaned: %s" % params
        return False

    def process(self, params):
        """
        Send to processor and return whatever we get back.
        """
        params = "processor_module_call_here(%s)" % params
        return params

    def validation_entry(self, params):
        validated = self.validate(params)
        cleaned = self.clean(validated)
        processed = self.process(cleaned)
        return processed


class Handler(webapp2.RequestHandler):

    def __init__(self, request, response):
        # Like calling super, but with the built-in for webapp2
        self.initialize(request, response)

        self.proc = Processor()

    def get(self):
        params = {
            'headers': self.request.headers,
            'body': self.request.body,
            'content-type': self.request.content_type,
            'query-string': self.request.query_string,
            'params': self.request.params
        }
        processed = self.proc.validation_entry(params)
        if processed:
            self.response.write("validated, cleaned, and processed GET data: %s" % processed)
        else:
            self.response.write('Error handling and appropriate status code would go here')

    def post(self):
        params = {
            'headers': self.request.headers,
            'body': self.request.body,
            'content-type': self.request.content_type,
            'query-string': self.request.query_string,
            'params': self.request.params
        }
        processed = self.proc.validation_entry(params)
        if processed:
            self.response.write("validated, cleaned, and processed POST data: %s" % processed)
        else:
            self.response.write('Error handling and appropriate status code goes here.')


if __name__ == '__main__':
    app = webapp2.WSGIApplication([
        ('/', Handler),
    ], debug=True)

    httpserver.serve(app, host='127.0.0.1', port='8080')