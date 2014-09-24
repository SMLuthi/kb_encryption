#!/usr/bin/env python
from encrypter_app import app
from flask import json
import unittest


# Test cases for encrypter_app webframework
class EncrypterTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_route_undefined(self):
        '''
        Test routes without a predefined endpoint
        '''
        rv = self.app.get('/random')
        assert rv.status_code == 404

    def test_enter_new_user(self):
        '''
        Test generic user creation
        '''
        rv = self.app.post('/keys/testUser')
        assert rv.status_code == 201
        data = json.loads(rv.data)['new_user']
        self.assertEqual(data['user'], 'testUser')
        self.assertIsNotNone(data['secret_key'])
        self.assertIsNotNone(data['created_on'])

    def test_enter_multiple_users(self):
        '''
        Test creation of multiple users back-to-back
        '''
        rv1 = self.app.post('/keys/multiUser1')
        rv2 = self.app.post('/keys/multiUser2')
        assert rv1.status_code == 201 and rv2.status_code == 201
        data = json.loads(rv1.data)['new_user']
        self.assertEqual(data['user'], 'multiUser1')
        self.assertIsNotNone(data['secret_key'])
        self.assertIsNotNone(data['created_on'])
        data = json.loads(rv2.data)['new_user']
        self.assertEqual(data['user'], 'multiUser2')
        self.assertIsNotNone(data['secret_key'])
        self.assertIsNotNone(data['created_on'])

    def test_duplicate_user(self):
        '''
        Test response when entering duplicate users
        '''
        rv1 = self.app.post('/keys/dupliUser')
        rv2 = self.app.post('/keys/dupliUser')
        assert rv1.status_code == 201 and rv2.status_code == 409
        data = json.loads(rv1.data)['new_user']
        self.assertEqual(data['user'], 'dupliUser')
        self.assertIsNotNone(data['secret_key'])
        self.assertIsNotNone(data['created_on'])

    def test_retrieve_user(self):
        '''
        Test retrieval of user data
        '''
        self.app.post('/keys/retrieveUser')
        rv = self.app.get('/keys/retrieveUser')
        assert rv.status_code == 200
        data = json.loads(rv.data)['search_result']
        self.assertEqual(data['user'], 'retrieveUser')
        self.assertIsNotNone(data['secret_key'])
        self.assertIsNotNone(data['created_on'])

    def test_retrive_dne_user(self):
        '''
        Test response when retrieving user that does not exist
        '''
        rv = self.app.get('/keys/dneUser')
        assert rv.status_code == 404
        data = json.loads(rv.data)
        self.assertEqual(data['error'], 'NotFound')
        self.assertEqual(data['error_msg'], 'User not found')

if __name__ == '__main__':
    unittest.main()
