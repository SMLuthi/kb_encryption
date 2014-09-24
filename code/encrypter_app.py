#!/usr/bin/env python
from flask import Flask, abort, jsonify, make_response
import os
import binascii
import datetime

app = Flask(__name__)

# Data structure to mock back end environment
user_list = []


def searcher(username):
    return filter(lambda u: u['user'] == username, user_list)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'NotFound',
                                  'error_msg': 'User not found'}), 404)


@app.errorhandler(409)
def duplicate_entry(error):
    return make_response(jsonify({'error': 'DuplicateEntry',
                                  'error_msg': 'Username already exists'}), 409)


# Retrieve user data endpoint
@app.route('/keys/<string:username>', methods=['GET'])
def get_key(username):
    # Search users to avoid generating duplicate user entries
    search = searcher(username)
    if len(search) == 0:
        abort(404)
    return jsonify({'search_result': search[0]})


# Add new user data endpoint
@app.route('/keys/<string:username>', methods=['POST'])
def gen_key(username):
    # Search users to avoid generating duplicate user entries
    search = searcher(username)
    if len(search) != 0:
        abort(409)

    # Generate a new user entry with a random 16 digit hex string and timestamp
    new_user = {
        'user': username,
        'secret_key': binascii.b2a_hex(os.urandom(8)),
        'created_on': datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    }

    user_list.append(new_user)

    return jsonify({'new_user': new_user}), 201


# Delete user data endpoint
@app.route('/keys/<string:username>', methods=['DELETE'])
def del_user(username):
    # Search in memory for existing user data
    search = searcher(username)
    if len(search) == 0:
        abort(404)

    user_list.remove(search[0])
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
