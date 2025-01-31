#!/usr/bin/python3
""" a script that starts Flask web application """
from flask import Flask, render_template


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
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is cool'):
    """ adds text uri after python route """
    if text != 'is cool':
        text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """ display number passed to url """
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ display html template with number """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """ display if number is odd or even inside template """
    context = {'n': n}
    if (n != 0 and n % 2 == 0):
        context['result'] = 'even'
    else:
        context['result'] = 'odd'
    return render_template('6-number_odd_or_even.html', context=context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
