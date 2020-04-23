#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def get_states_by_city():
    """"""
    states_dict = {}
    dict_values = storage.all(State).values()
    dict_values = sorted(dict_values, key=lambda x: x.name)
    state_cities = []
    for state in dict_values:
        list_city = state.cities
        list_city = tuple(sorted(list_city, key=lambda x: x.name))
        pair = (state, list_city)
        state_cities.append(pair)

    return render_template('8-cities_by_states.html', state=state_cities)


@app.teardown_appcontext
def close(error):
    storage.close()

if __name__ == "__main__":
    """main"""
    app.run(host='0.0.0.0', port=5000)
