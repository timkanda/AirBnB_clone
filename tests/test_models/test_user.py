#!/usr/bin/python3
"""unittest for user"""

from models.base_model import BaseModel
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def test_attributes(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == '__main__':
    unittest.main()
