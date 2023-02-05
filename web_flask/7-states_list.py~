#!/usr/bin/python3
'''crates a flask web application'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes=False

@app.route('/states_list')
def display_states():
    return render_template('7-states_list.html', storage=storage.all('State'))

@app.teardown_appcontext
def close(exception):
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')
