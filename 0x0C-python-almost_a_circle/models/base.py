#!/usr/bin/python3

"""class base"""
import json
import csv


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
            list_objs = []

        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            jstring = cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs])
            f.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string representation"""
        if json_string is None or len(json_string) == 0:
            return []
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
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saves to csv file"""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline="") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldheads = ["id", "width", "height", "x", "y"]
                else:
                    fieldheads = ["id", "size", "x", "y"]

                writes = csv.Dictwriter(f, fieldheads=fieldheads)
                for obj in list_objs:
                    writes.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """reads from csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as f:
                if cls.__name__ == "Rectangle":
                    fieldheads = ["id", "width", "height", "x", "y"]
                else:
                    fieldheads = ["id", "size", "x", "y"]

                lst = csv.DictReader(f, fieldheads=fieldheads)

                lst = [dict([k, int(v)] for k, v in d.items())
                        for d in lst]
                return [cls.create(**d) for d in lst]
        except IOError:
            return []

