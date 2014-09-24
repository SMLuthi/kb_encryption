[![Build Status](https://travis-ci.org/SMLuthi/kb_encryption.svg?branch=master)](https://travis-ci.org/SMLuthi/kb_encryption)

# kb_encryption

## Description

Simple REST API to create/read/delete secret keys.

## Requirements

* Python 2.7
* virtualenv (suggested)

## Installation

_Using GIT Clone_

In your `workspace` directory type:

	- git clone -b master git@github.com:SMLuthi/kb_encryption.git kb_encryption
	- mkvirtualenv kb_encryption
	- cd into kb_encryption
	- pip install -r requirements.txt --no-index

## Usage

_Start Encrypter API_

	- ./<repo root>/code/encrypter_app.py

_Simple tests_

	- curl -i -H "Content-Type: applicationn/json" -X POST http://localhost:5000/keys/testUser -u "admin:password"
	- curl -i -H "Content-Type: applicationn/json" http://localhost:5000/keys/testUser -u "admin:password"
	- curl -i -H "Content-Type: applicationn/json" -X DELETE http://localhost:5000/keys/testUser -u "admin:password"
