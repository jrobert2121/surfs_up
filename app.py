# import dependencies
from flask import Flask

# create new Flask instance
app = Flask(__name__)

# define root
@app.route('/')
def hello_world():
    return 'Hello world'

