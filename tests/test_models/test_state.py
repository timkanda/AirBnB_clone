#!/usr/bin/python3
"""unittest for state"""

from models.base_model import BaseModel
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Defines the tests for the State class."""

    def setUp(self):
        """Sets up the testing environment."""
        self.test_state = State()

    def test_state_inherits_from_base_model(self):
        """Tests that State inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.test_state), BaseModel))

    def test_state_has_attribute_name(self):
        """Tests that State has an attribute 'name'."""
        self.assertTrue(hasattr(self.test_state, "name"))
        self.assertIsInstance(self.test_state.name, str)

    def test_state_attribute_name_initial_value(self):
        """Tests that the initial value of the 'name'
                attribute is an empty string."""
        self.assertEqual(self.test_state.name, "")


if __name__ == '__main__':
    unittest.main()
