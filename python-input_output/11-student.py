#!/usr/bin/python3

"""
class Student that defines a student
"""


class Student:
    """
    class Student that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Pick the attributes of the students class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student instance
        """
        attr_order = ["first_name", "last_name", "age"]
        result = {}

        if attrs is None:
            for attr in attr_order:
                result[attr] = getattr(self, attr)
        else:
            for attr in attr_order:
                if attr in attrs:
                    result[attr] = getattr(self, attr)

        return result

    def reload_from_json(self, json):
        """
        replaces all attributes of the Student instance
        """
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
