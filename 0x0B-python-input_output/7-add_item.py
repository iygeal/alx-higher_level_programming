#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a file.
"""
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    def add_item():
        """
        Adds all command-line arguments to a Python list
        and saves it to a JSON file.
        """
        try:
            # Load existing list from file, if any
            existing_list = load_from_json_file("add_item.json")
        except FileNotFoundError:
            existing_list = []

        # Add command-line arguments to the list
        new_items = sys.argv[1:]
        updated_list = existing_list + new_items

        # Save the updated list to the JSON file
        save_to_json_file(updated_list, "add_item.json")
