#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4  # Import the downloaded .pyc file
    defined_names = dir(hidden_4)  # Use dir() to get the names
    for name in defined_names:  # Iterate through the defined names
        if name[0:2] == "__":  # Check if first 2 characters are underscores
            continue  # If they are, skip the name and go to next
        print(name)  # Print all names (which don't start with underscores)``
