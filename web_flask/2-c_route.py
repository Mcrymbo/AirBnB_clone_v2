#!/usr/bin/python3
# a script that starts Flask web application
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """a function that defines / route """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ defines /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """ allows a text to be passed in the url """
    return 'C is {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
