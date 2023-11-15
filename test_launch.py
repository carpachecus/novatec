''' This module contains tests for the Flask app in launch.py'''

# 1. Import libraries
import unittest
from launch import app


# 2. Define a test class
class TestLaunch(unittest.TestCase):

    # 3. Define a test method
    def test_index(self):
        '''Test that the index page returns a welcome message and the current time.'''
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'<h1>Welcome to my Credibanco web app!</h1>', response.data)
            self.assertIn(b'<h1>The current time is', response.data)

    # 4. Define another test method
    def test_index_content(self):
        '''Test that the index page contains the correct content.'''
        with app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'text/html; charset=utf-8')
            self.assertIn(b'<h1>Welcome to my Credibanco web app!</h1>', response.data)
            self.assertIn(b'<h1>The current time is', response.data)