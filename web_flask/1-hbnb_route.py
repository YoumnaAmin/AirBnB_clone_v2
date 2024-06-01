#!/usr/bin/python3
"""0-hello module

This module starts a Flask web application that returns "Hello HBNB!"
when accessing the root URL.
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Home page route that returns 'Hello HBNB!'"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    """display HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(debug=False)
