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
        # If attrs is None or empty, retrieve all attributes
        if attrs is None or not attrs:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }

        # Retrieve only the specified attributes from the list
        return {
            attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)
            }
