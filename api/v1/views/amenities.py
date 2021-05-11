#!/usr/bin/python3

from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import abort, jsonify, make_response, request

@app_views.route('/amenities', strict_slashes=false, methods=['GET'])
def amenities_get():
    """use the id to search for a user"""
    A = storage.all("Amenity")
    list = []
    for amenity in amenities.values():
        list.append(amenity.to_dict)
    if i is None:
        abort(404)
    return jsonify(list, i.to_dict())

@app_views.route('/amenities/<amenity_id>', strict_slashes=false, methods=['DELETE'])
def delete_am_id(amenity_id):
    """delete amenity id"""
    A = storage.get(Amenity, amenity_id)
    if i is None:
        abort(404)
    A.delete()
    storage.save()
    return jsonify({})


@app_views.route('amenities', strict_slashes=false, methods=['POST'])
def post_a_id():
    """amenity id and states"""
    A = storage.get(state, state_id)
    dict = request.get_json()
    if i is None:
        abort(404)
    if not dict:
        return make_response(jsonify({'error': Not a JSON}), 400)
    if "name" not in dict:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    dict["state_id"] = state_id
    new_user = Amenity(**dict)
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)

@app_views.route('/amenities/<amenity_id>', strict_slashes=false, methods=['PUT'])
def amenity_update(amenity_id):
    """update city"""
    dict = request.get_json()
    A = storage.get(Amenity, amenity_id)
    if i is None:
        abort (404)
    if not dict:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ["id", "created_at", "update_at"]:
            setattr(A, key ,sict[key])
    A.save()
    return jsonify(i.to_dict)
