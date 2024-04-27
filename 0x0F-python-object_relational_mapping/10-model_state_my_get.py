#!/usr/bin/python3
"""Prints the State object with the given name"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    # Extract arguments
    user, passwd, db_name, state_name = argv[1], argv[2], argv[3], argv[4]

    # Create Database connection URL
    db_url = f"mysql://{user}:{passwd}@localhost:3306/{db_name}"

    # Create engine and establish connection to database
    engine = create_engine(db_url)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query State object with the given name
        state = session.query(State).filter(State.name == state_name).first()

        # Check if state exists
        if state:
            print(state.id)
        else:
            print("Not found")

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
