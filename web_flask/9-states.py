#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def get_states():
    """"""
    states_dict = {}
    dict_values = storage.all(State).values()
    for item in dict_values:
        ids = item.id
        state = item.name
        states_dict[ids] = state
    sorted_tuple = sorted(states_dict.items(), key=lambda x: x[1])
    list_cities = []
    state_city = []

    return render_template('9-states.html',
                           sorted_dict=sorted_tuple,
                           list_cities=list_cities)


@app.route('/states/<id>', strict_slashes=False)
def get_state_by_id(id=None):
    """"""
    states_dict = {}
    dict_values = storage.all(State).values()
    dict_values = sorted(dict_values, key=lambda x: x.name)
    for state in dict_values:
        if state.id == id:
            list_cities = state.cities
            list_cities = tuple(sorted(list_cities, key=lambda x: x.name))
            state_city = state
            break
        else:
            list_cities = []
            state_city = []
    return render_template('9-states.html',
                           list_cities=list_cities,
                           state=state_city, h1="Not found!")


@app.teardown_appcontext
def close(error):
    storage.close()

if __name__ == "__main__":
    """main"""
    app.run(host='0.0.0.0', port=5000)
