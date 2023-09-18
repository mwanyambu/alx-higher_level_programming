#!/usr/bin/python3

"""class base"""
import json


class Base:
    """define base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """class constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """convert to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string representation"""
        if list_objs is None:
            return "[]"

        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            jstring = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            f.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create instances with attributes from dictionary"""
        if cls.__name__ == "Rectangle":
            dict_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dict_instance = cls(1)

        dict_instance.update(**dictionary)
        return dict_instance

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as f:
                jdata = f.read()
                dictionaries = cls.from_json_string(jdata)
                instances = [cls.create(**dictionary) for dic in dictionaries]
                return instances
        except FileNotFoundError:
            return "[]"
