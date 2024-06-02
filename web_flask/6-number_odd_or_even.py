#!/usr/bin/python3
"""0-hello module

This module starts a Flask web application that returns "Hello HBNB!"
when accessing the root URL.
"""

from flask import Flask, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """display c followed by text"""
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def n_int(n):
    """display only int numbers"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_n(n):
    """display through templates"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    """display odd or even"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(debug=False)
