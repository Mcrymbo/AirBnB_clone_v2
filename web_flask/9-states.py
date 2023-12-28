#!/usr/bin/python3
"""
fetches data from storage engine and serves them using flask
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id=None):
    """ A function that gets cities by states """
    states = storage.all(State)

    if not id:
        states = {value.id: value.name for value in states.values()}
        return render_template('7-states.html',
                           Table="States", items=states)

    id_name = 'State.{}'.format(id)
    if id_name in states:
        return render_template('9-states.html', Table='States',
                               items=states[id_name])
    return render_template('9-states.html', items=None)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
