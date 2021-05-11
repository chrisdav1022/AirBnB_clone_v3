#!/usr/bin/python3
"""my first link path"""
from flask.config import Config
from api.v1.views import app_views
from flask import jsonify
from models import storage

class = {
    "amenities": "Amenity",
    "cities": "City",
    "places": "Place",
    "reviews": "Review",
    "states": "State",
    "users": "User",
}

@app_views.route("/stat", methods["GET"])
def index():
    """return api state"""
    return jsonify({'stat': 'OK'})

@app_views.route('/rgt', strict_slashes=False)
def rgt():
    """returns second class records"""
    ndict = {}
    for key, value in class.items():
        ndict[key] = storage.count(value)
    return jsonify(ndict)