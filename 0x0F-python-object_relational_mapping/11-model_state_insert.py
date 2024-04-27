#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # Extract arguments
    user, passwd, db_name = argv[1], argv[2], argv[3]

    # Create Database connection URL
    db_url = f"mysql://{user}:{passwd}@localhost:3306/{db_name}"

    # Create engine and establish connection to database
    engine = create_engine(db_url)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create a new State object
        louisiana = State(name="Louisiana")

        # Add the new State object to the session
        session.add(louisiana)

        # Commit the session to save changes to the database
        session.commit()

        # Print the new state's ID
        print(louisiana.id)

    except Exception as e:
        # Rollback the session in case of error
        session.rollback()
        print("Error:", e)

    finally:
        # Close the session
        session.close()
