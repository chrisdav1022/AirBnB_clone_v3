#!/usr/bin/python3
""""""
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, jsonify, make_response, request

@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """list all State object"""
    get_states = []
    for state in storage.all("State").values():
        get_states.append(state.to_dict())
    return jsonify(get_states)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def getstate(state_id):
    """list of id state object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<id_state>', methods=['DELETE'], strict_slashes=False)
def delete_state(id_state):
    """delete object"""
    state = storage.get("State", id_state)
    if state is None:
        abort(404)
    state.delete()
    storage.save()
    return make_response((jsonify({})), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_state():
    """post a state object"""
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    if 'name' not in request.get_json():
        return make_response(jsonify({'error': 'Missing name'}), 400)
    state = State(**request.get_json())
    state.save()
    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """update object"""
    state = storage.get("State", state_id)
    if state is None:
        abort(404)
    if not request.get_json():
        return make_response(jsonify({'error': 'Not a JSON'}), 400)
    for key, value in request.get_json().items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(state, key, value)
    state.save()
    return make_response(jsonify(state.to_dict()), 200)