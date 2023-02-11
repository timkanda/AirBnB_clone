#!/usr/bin/python3
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

        class_dict = {"BaseModel": BaseModel}
        obj = {}
        try:
            with open(FileStorage.__file_path, "r") as f:
                json_data = json.load(f)
                for key, value in json.data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
                FileStorage.__objects = obj
        except FileNotFoundError:
            pass
