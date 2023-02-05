#!/usr/bin/python3
"""  script that starts a Flask web application """

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', strict_slashes=False)
def hello():
    """ hello HBNB! """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ HBNB! """
    return ('HBNB!')


@app.route('/c/<text>')
def c_is_fun(text):
    return ('C %s' % text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_is_cool(text):
    return ('Python %s' % text.replace("_", " "))


@app.route('/number/<int:n>')
def num(n):
    return ('%d is a number' % n)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
