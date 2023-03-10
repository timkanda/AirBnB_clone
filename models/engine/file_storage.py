#!/usr/bin/python3
"""serializes and deserializes objects to
and from json
"""


import json


class FileStorage:
    """serializes and deserializes JSON file."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary."""
        return (FileStorage.__objects)

    def new(self, obj):
        """creates object."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes object to JSON file."""
        my_dict = {}
        for key, value in FileStorage.__objects.items():
            my_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:

            json.dump(my_dict, f)

    def reload(self):
        """deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }
        obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, "r") as d:
                json_data = json.load(d)
                for key, value in json_data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
