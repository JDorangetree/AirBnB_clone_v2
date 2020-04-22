#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from flask import Flask
from flask import render_template
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states():
    """"""
    states_dict = {}
    dict_values = storage.all(State).values()
    for item in dict_values:
        ids = item.id
        state = item.name
        states_dict[ids] = state
    sorted_tuple = sorted(states_dict.items(), key=lambda x: x[1])
    return render_template('7-states_list.html', sorted_dict=sorted_tuple)


@app.teardown_appcontext
def close(error):
    storage.close()

if __name__ == "__main__":
    """main"""
    app.run(host='0.0.0.0', port=5000)
