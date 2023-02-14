#!/usr/bin/python3
"""unittest for base_model"""

import uuid
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_id_generation(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_save_method(self):
        bm = BaseModel()
        created_at = bm.created_at
        updated_at = bm.updated_at
        bm.save()
        self.assertGreater(bm.updated_at, updated_at)
        self.assertEqual(bm.created_at, created_at)

    def test_to_dict_method(self):
        bm = BaseModel()
        my_dict = bm.to_dict()
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict['__class__'], 'BaseModel')
        self.assertIsInstance(my_dict['created_at'], str)
        self.assertIsInstance(my_dict['updated_at'], str)


if __name__ == '__main__':
    unittest.main()
