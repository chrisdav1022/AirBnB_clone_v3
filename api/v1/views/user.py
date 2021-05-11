#!/usr/bin/python3
"""views web page"""
from api.v1.views import app_views
from models import storage
from models.user import User
from models.state import state
from flask import abort, jsonify, make_response, request

@app_views.route('/users', strict_slashes=false, methods=['GET'])
def list_u():
    """use the id to list for a user"""
    us = storage.all("User")
    list = []
    for amenity in amenities.values():
        list.append(amenity.to_dict)
    if us is None:
        abort(404)
    return jsonify(list, i.to_dict())

@app_views.route('/users/<user_id>', strict_slashes=false, methods=['DELETE'])
def delete_user(user_id):
    """delete amenity id"""
    us = storage.get(user, user_id)
    if us is None:
        abort(404)
    us.delete()
    storage.save()
    return jsonify({})


@app_views.route('/users', strict_slashes=false, methods=['POST'])
def post_us_id():
    """user id and states"""
    dict = request.get_json()
    if i is None:
        abort(404)
    if not dict:
        return make_response(jsonify({'error': Not a JSON}), 400)
    if "email" not in dict:
        return make_response(jsonify({'error': 'Missing name'}), 400)
    if "password" not in dict:
        return make_response(jsonify({'error': 'Missing password'}), 400)

    new_user = User(**dict)
    print(User(**dict))
    new_user.save()
    return make_response(jsonify(new_user.to_dict()), 201)

@app_views.route('/user/<user_id>', strict_slashes=false, methods=['PUT'])
def user_update(amenity_id):
    """update user"""
    dict = request.get_json()
    us = storage.get(User, user_id)
    if us is None:
        abort (404)
    if not dict:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key in dict.keys():
        if key not in ["id", "email", "created_at", "update_at"]:
            setattr(us, key ,dict[key])
    us.save()
    return jsonify(us.to_dict)
