#!/usr/bin/python3
"""0-hello module"""


from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """home page"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(debug=False)
