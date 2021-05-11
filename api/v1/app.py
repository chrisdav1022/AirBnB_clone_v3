#!/usr/bin/python3
"""in  the code start my api"""

from flask import Flask, jsonify, render_template, make_response
from models import storage
from api.v1.views import app_views
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def close(error):
    """close"""
    storage.close()


@app.errorhandler(404)
def page_not_found(e):
    """ page not found """
    return make_response(jsonify({'error': "Not found"}), 404)


if __name__ == '__main__':
    """ run the main flask """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)