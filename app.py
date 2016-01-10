# ---- Flask Hello World! ---- #

# Import the Flask class from the flask package
from flask import Flask

# Create the application object
app = Flask(__name__)

# use decorators to link the function to a URL
@app.route('/')
@app.route('/hello')

# define the view using a function that returns a string
def hello_world():
    return "Hello World!"

# start the development server using the run method 
if __name__ == "__main__":
    app.run()
