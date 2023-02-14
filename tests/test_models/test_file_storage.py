#!/usr/bin/python3
"""unittest for file_storage"""

import os
import unittest
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.file_path = FileStorage._FileStorage__file_path
        self.storage = FileStorage()

    def test_all(self):
        all_objs = self.storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIs(all_objs, self.storage._FileStorage__objects)

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIs(self.storage.all()[key], obj)

    def test_save_reload(self):
        self.storage.save()
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
        self.assertGreater(len(lines), 0)
        os.remove(self.file_path)

        obj = State()
        obj.name = "California"
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, all_objs)

    def test_reload_no_file(self):
        os.remove(self.file_path)
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_from_file(self):
        obj = User()
        obj.email = "test@test.com"
        obj.password = "password"
        obj.first_name = "Test"
        obj.last_name = "User"
        self.storage.new(obj)
        self.storage.save()

        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, all_objs)
        self.assertEqual(all_objs[key].email, obj.email)
        self.assertEqual(all_objs[key].password, obj.password)
        self.assertEqual(all_objs[key].first_name, obj.first_name)
        self.assertEqual(all_objs[key].last_name, obj.last_name)


if __name__ == '__main__':
    unittest.main()
