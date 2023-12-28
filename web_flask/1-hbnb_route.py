#!/usr/bin/python3
"""Initiates a Flask Web App named HBNB"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays a message upon accessing /"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays a message upon accessing /hbnb"""
    return 'HBNB'

if __name__ == "__main__":
    """Entry point for execution"""
    app.run(host='0.0.0.0', port=5000)
