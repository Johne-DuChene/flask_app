'''this is the app's main file, used for
    storing the logic.'''

# the import
from flask import Flask

# instantiate the app
'''the first argument of the class is the
    name of the app's module or package,
    which __name__ is a shortcut for.'''
app = Flask(__name__)

# decorator to define what happens at the
# home directory
@app.route("/")
def hello_world():
    # returns the string "Hello, World!"
    return 'Hello, World!'

# use the route() deco to
# bind a function to a url
@app.route("/index")
def index():
    return 'Index Page'