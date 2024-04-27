#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects in the database
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
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
        # Query all State objects with their corresponding City objects
        states = session.query(State).order_by(State.id).all()

        # Print the results
        for state in states:
            print(f"{state.id}: {state.name}")
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        session.close()
