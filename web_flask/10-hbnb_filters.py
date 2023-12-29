#!/usr/bin/python3
"""
fetches data from storage engine and serves them using flask
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route('/hbnb_filters/', strict_slashes=False)
def hbnb_filter():
    """ handles /hbnb_filters route """
    states = storage.all(State)
    amenities = storage.all(Amenity)

    return render_template('10-hbnb_filters.py', state=states.values(),
                           amenities=amenities.values())


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
