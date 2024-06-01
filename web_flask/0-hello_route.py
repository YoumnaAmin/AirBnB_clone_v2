#!/usr/bin/python3
"""0-hello module"""


from flask import Flask


app = Flask(__name__)
@app.route("/")
def hello_hbnb():
    """home page"""
    return "<h1>Hello HBNB!</h1>"


if __name__ == '__main__':
    app.run()
