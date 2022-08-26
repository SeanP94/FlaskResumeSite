'''
Preweekend final prep:
***DO NOT CONTINUE CODING THIS FILE, WITHOUT A GITHUB REPO***

Flask:
    Keep familiarizing.


Pico8: #Going to include also weekend work as well...
    Try to get xforce working.
    Aerial* Bouncing off walls. (only works if jumping)

    PICOBUGS:
        If standing under a long wall, if I jump at the right pixel itll clip into the wall. Need to fix.
            --Fix AFTER the xforce is working. Because it's probably a variable issue, so if I get xforce
                working first, then the bug should stay fixed after I fix it.

Html&CSS:
    Pick a good online website template.
    Pick a color pallet

    Try to finish a CSS course and intermediate CSS on Codecademy.

JS:
    g2g

Weekend Goal:
    Have SOMETHING that looks like an okay website.
    Use Codepen:


'''
from flask import Flask # And templates..
app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Hello World</h1>"


# TODO:
# Make this a link from the resume project page. 
@app.route('/jumpgame')
def jumpgame():
    pass