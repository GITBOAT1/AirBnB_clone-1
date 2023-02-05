#!/usr/bin/python3
'''crates a flask web application'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)

app.jinja_env.lstrip_blocks = True


@app.route('/states_list')
def display_states():
    return render_template('7-states_list.html', storage=storage.all('State'))


@app.route('/cities_by_states')
def display_cities_by_states():
    return render_template('8-cities_by_states.html',
                           storage=storage.all('State'))


@app.teardown_appcontext
def close(exception):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
