import os
import logging
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment (
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):

    def get(self):
        template = JINJA_ENVIRONMENT.get_template('templates/index.htm')
        self.response.write(template.render({'hint': 'Good luck!'}))

    def post(self):
        stguess = self.request.get('guess')
        try:
            guess = int(stguess)
        except:
            guess = -1

        answer = 42
        if guess == answer:
            msg = 'Congratulations'
        elif guess < 0 :
            msg = 'Please provide a number guess'
        elif guess < answer:
            msg = 'Your guess is too low'
        else:
            msg = 'Your guess is too high'

        template_values = {
            'hint': msg,
            'stguess': stguess,
        }
        template = JINJA_ENVIRONMENT.get_template('templates/guess.htm')
        self.response.write(template.render(template_values))

app = webapp2.WSGIApplication([
        ('/', MainHandler),
    ], debug=True)