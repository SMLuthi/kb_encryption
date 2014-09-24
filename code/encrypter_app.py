#!/usr/bin/env python
from flask import Flask, abort

app = Flask(__name__)

# Data structure to mock back end environment
user_list = []


# Retrieve user data endpoint
@app.route('/keys/<string:username>', methods=['GET'])
def get_key(username):
    abort(503)


# Add new user data endpoint
@app.route('/keys/<string:username>', methods=['POST'])
def gen_key(username):
    abort(503)


# Delete user data endpoint
@app.route('/keys/<string:username>', methods=['DELETE'])
def del_user(username):
    abort(503)

if __name__ == '__main__':
    app.run(debug=True)
