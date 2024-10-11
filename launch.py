''' This module contains a Flask app that displays
a welcome message and the current time'''

# 1. Import libraries
from flask import Flask
from datetime import datetime

# 2. Create a Flask app
app = Flask(__name__)


# 3. Define a route and a view function
@app.route('/')
def index():
    '''This function returns a welcome message and the current time.'''
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f'<h1>Welcome to Carlos Pacheco App!</h1><h1>The current time is {current_time}.</h1>'

# 4. Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int("5000"))
