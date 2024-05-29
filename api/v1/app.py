#!/usr/bin/python3
"""Module to create a flask app"""

from api.v1.views import app_views
from flask import Flask
from  models import storage
import os


# create a variable app, instance of Flask
app = Flask(__name__)

# register the blueprint app_views to your Flask instance app
app.register_blueprint(app_views)


# handle @app.teardown_appcontext that calls storage.close()
@app.teardown_appcontext
def teardown_db(exception):
    """Method to handle teardown of app context"""
    storage.close()


# Run the app
if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', '5000'))

    # Start the Flask server
    app.run(host=host, port=port, threaded=True)