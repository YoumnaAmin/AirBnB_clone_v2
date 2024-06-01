#!/usr/bin/python3
"""0-hello module

This module starts a Flask web application that returns "Hello HBNB!"
when accessing the root URL.
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Home page route that returns 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def slash_hbnb():
    """display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """display c followed by text"""
    return f"C {escape(text.replace('_', ' '))}"


if __name__ == '__main__':
    app.run(debug=False)
