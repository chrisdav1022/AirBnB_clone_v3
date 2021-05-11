#!/usr/bin/python3

from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from flask import abort, jsonify, make_response, request

@app_views.route('/cities/<city_id>', strict_slashes=false, methods=['GET'])
def city_id(city_id):
    """use the id to search for a city"""
    i = storage.get(City, city_id)
    if i is None:
        abort(404)
    return jsonify(i.to_dict())

@app_views.route('/cities/<city_id>', strict_slashes=false, methods=['DELETE'])
def delete_c_id(city_id):
    """delete city id"""
    i = storage.get(City, city_id)
    if i is None:
        abort(404)
    i.delete()
    storage.save()
    return jsonify({})


@app_views.route('states/<state_id>/cities', strict_slashes=false, methods=['POST'])
def post_c_id(state_id):
    """city id and states"""
    i = storage.get(state, state_id)
    dict = request.get_json()
    if i is None:
        abort(404)
    if not dict:
        return make_response(jsonify({'error': not a JSON}), 400)
    if "name" not in dict:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    dict["state_id"] = state_id
    new_city = City(**dict)
    print(City(**dict))
    new_city.save()
    return make_response(jsonify(new_city.to_dict()), 201)

@app_views.route('/cities/<city_id>', strict_slashes=false, methods=['PUT'])
def city_update(city_id):
    """update city"""
    dict = request.get_json()
    i = storage.get(City, city_id)
    if i is None:
        abort (404)
    if not dict:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key in dict.keys():
        if key not in ["id", "state_id", "created_at", "update_at"]:
            setattr(i, key ,sict[key])
    i.save()
    return jsonify(i.to_dict)