#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
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
        # Query all City objects and join with
        # State objects using the relationship
        cities = session.query(City).order_by(City.id).all()

        # Print results
        for city in cities:
            state_name = city.state.name
            print(f"{city.id}: {city.name} -> {state_name}")

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the session
        session.close()
