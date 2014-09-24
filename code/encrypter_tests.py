#!/usr/bin/env python
from encrypter_app import app
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

if __name__ == '__main__':
    unittest.main()
