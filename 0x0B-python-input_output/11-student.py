#!/usr/bin/python3
"""
Module to define the Student class.
"""


class Student:
    """
    Class to define a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with first_name, last_name,
        and age attributes.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): A list of attribute names to be retrieved. If None,
            retrieve all attributes.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        # Check if attrs is a list of strings
        if isinstance(
                attrs, list) and all(isinstance(ele, str) for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}

        # Return the entire __dict__ if attrs is not a valid list of strings
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with the values
        from a dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values.

        Returns:
            None
        """
        # Replace attributes with values from the json dictionary
        for key, value in json.items():
            setattr(self, key, value)
