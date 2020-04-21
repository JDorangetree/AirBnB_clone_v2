#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ Prints a Message when / is called """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """main"""
    app.run(host='0.0.0.0', port=5000)
