#!/usr/bin/python3
"""Initiates a Flask Web App"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays a message upon accessing /"""
    return 'Hello HBNB!'

if __name__ == "__main__":
    """Entry point"""
    app.run(host='0.0.0.0', port=5000)
