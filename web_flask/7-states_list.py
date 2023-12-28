#!/usr/bin/python3
"""
fetches data from storage engine and serves them using flask
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    states = storage.all(State)
    context = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html', Table="States", items=context)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
