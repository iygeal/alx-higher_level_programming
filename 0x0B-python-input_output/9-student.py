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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: A dictionary representation of the Student instance.
        """
        # Create a dictionary with serializable attributes
        serializable_dict = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

        return serializable_dict
