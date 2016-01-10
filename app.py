# ---- Flask Hello World! ---- #

# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# error handling 
app.config['DEBUG'] = True

# use decorators to link the function to a URL
@app.route('/')
@app.route('/hello')
# define the view using a function that returns a string
def hello_world():
    return "Hello World!"


# dynamic route
@app.route('/test/<search_query>')
def search(search_query):
    return search_query

# flask converters
@app.route('/integer/<int:value>')
def int_type(value):
    print value + 1
    return 'correct'


@app.route('/float/<float:value>')
def float_type(value):
    print value + 1
    return 'correct'

# dynamic route that accepts slashes
@app.route('/path/<path:value>')
def path_type(value):
    print value
    return 'correct'


# response object is a tuple (response, status= (int)HTTP status code, headers = dictionary)
@app.route('/name/<name>')
def index(name):
    if name.lower() == 'javier':
        return 'Hello {}!'.format(name)
    else:
        return 'Not found', 404


# start the development server using the run method
if __name__ == "__main__":
    app.run()
