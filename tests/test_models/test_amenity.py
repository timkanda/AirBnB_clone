#!/usr/bin/python3
"""unittest for amenity"""

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests the Amenity class."""

    def setUp(self):
        """Sets up the testing environment."""
        self.amenity = Amenity()

    def test_amenity_inherits_from_base_model(self):
        """Tests that Amenity inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_amenity_has_attribute_name(self):
        """Tests that Amenity has an attribute 'name'."""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertIsInstance(self.amenity.name, str)

    def test_amenity_attribute_name_initial_value(self):
        """Tests that the initial value of the 'name'
                attribute is an empty string."""
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
