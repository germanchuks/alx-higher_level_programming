#!/usr/bin/python3
"""Module for Base"""
import json
import csv


class Base:
    """
    The Base class for all other classes.

    Attributes:
        __nb_objects (int): A class attribute to keep track of the number of
        objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a new Base instance.

        Args:
            id (int, optional): An optional ID for the instance. If id is
            None, a unique ID is assigned based on the class attribute
            __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.
        """
        if not list_dictionaries:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a list of objects to a file.
        """
        file_name = f"{cls.__name__}.json"
        with open(file_name, mode='w', encoding='utf-8') as myFile:
            if list_objs:
                list_objs_dict = [obj.to_dictionary() for obj in list_objs]
                myFile.write(cls.to_json_string(list_objs_dict))
            else:
                myFile.write(cls.to_json_string([]))

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of a JSON string representation.
        """
        if not json_string:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all attributes already set.
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return (dummy_instance)

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, encoding="utf-8") as myFile:
                json_string = myFile.read()
                dict_list = cls.from_json_string(json_string)
                instance_list = [cls.create(**obj) for obj in dict_list]
                return (instance_list)
        except (FileNotFoundError, FileExistsError):
            return ([])

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Serializes in CSV.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', encoding='utf-8') as myCSVFile:
            if list_objs == [] or list_objs is None:
                myCSVFile.write(cls.to_json_string([]))
            else:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                dict_write = csv.DictWriter(myCSVFile, fieldnames=attr)
                for obj in list_objs:
                    dict_write.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserializes in CSV.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, newline='', encoding="utf-8") as myCSVFile:
                if cls.__name__ == "Rectangle":
                    attr = ["id", "width", "height", "x", "y"]
                else:
                    attr = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(myCSVFile, fieldnames=attr)
                list_dicts = [dict([attr, int(value)]
                              for attr, value in obj.items())
                              for obj in list_dicts]
                return ([cls.create(**obj) for obj in list_dicts])
        except (FileNotFoundError, FileExistsError):
            return ([])
