#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":

    # Extract arguments
    user, passwd, db_name = argv[1], argv[2], argv[3]

    # Create Database connection url
    db_url = f"mysql://{user}:{passwd}@localhost:3306/{db_name}"

    # Create engine and establish connection to database
    engine = create_engine(db_url)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query the first State object based on states.id
        state = session.query(State).order_by(State.id).first()

        # Check if state exists
        if state is not None:
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
