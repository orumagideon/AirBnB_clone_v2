Flask is a lightweight and versatile web framework for Python. It simplifies web development by offering tools and libraries to build web applications quickly and efficiently. It's known for its simplicity, flexibility, and ease of learning.

Key Features
Routing: Easily map URLs to Python functions.
HTTP Request Handling: Simple handling of HTTP requests and responses.
Template Engine: Jinja2 templating for creating dynamic web pages.
Extensible: A modular design with built-in support for extensions.
Development Server: Built-in server for easy testing and development.
RESTful Support: Flexible support for building REST APIs.
Secure: Provides tools to protect against common web vulnerabilities.
Installation
bash
Copy code
pip install flask
Quick Start
python
Copy code
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
