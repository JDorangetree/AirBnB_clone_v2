#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_world2():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_world3(text):
    text = text.replace("_", " ")
    return ("C {}".format(text))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_world4(text=None):
    if not text:
        text = "is cool"
    text = text.replace("_", " ")
    return ("Python {}".format(text))


@app.route('/number/<int:n>', strict_slashes=False)
def hello_world5(n):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def hello_world6(n):
    return render_template('5-number.html', n=n)

app.run(host='0.0.0.0', port=5000)
