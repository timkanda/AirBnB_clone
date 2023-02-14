#!/usr/bin/python3
"""unittest for city"""

from models.base_model import BaseModel
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Tests the City class."""

    def setUp(self):
        """Sets up testing environment."""
        self.city = City()

    def test_city_inherits_from_base_model(self):
        """Tests that City inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_city_has_attribute_state_id(self):
        """Tests that City has an attribute 'state_id'."""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertIsInstance(self.city.state_id, str)

    def test_city_has_attribute_name(self):
        """Tests that City has an attribute 'name'."""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertIsInstance(self.city.name, str)

    def test_city_attribute_state_id_initial_value(self):
        """Tests that the initial value of the 'state_id'
                attribute is an empty string."""
        self.assertEqual(self.city.state_id, "")

    def test_city_attribute_name_initial_value(self):
        """Tests that the initial value of the 'name'
                attribute is an empty string."""
        self.assertEqual(self.city.name, "")


if __name__ == '__main__':
    unittest.main()
