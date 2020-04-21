#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
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

if __name__ == "__main__":
    """main"""
    app.run(host='0.0.0.0', port=5000)
