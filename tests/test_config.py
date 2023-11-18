import unittest
from flask import current_app
from app import create_app, db

class TestDevelopmentConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app('development')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_is_development(self):
        self.assertFalse(current_app is None)
        self.assertTrue(current_app.config['DEBUG'] is True)

class TestTestingConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_is_testing(self):
        self.assertFalse(current_app is None)
        self.assertTrue(current_app.config['TESTING'] is True)

class TestProductionConfig(unittest.TestCase):
    def setUp(self):
        self.app = create_app('production')
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app_is_production(self):
        self.assertFalse(current_app is None)
        self.assertFalse(current_app.config['DEBUG'])

if __name__ == '__main__':
    unittest.main()
