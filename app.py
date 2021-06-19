# Import Flask
from flask import Flask

# Create a new Flask app instance
app = Flask(__name__)

# Create a Flask route
@app.route('/')
def hello_world():
    return 'Hello World'