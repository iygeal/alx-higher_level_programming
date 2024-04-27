#!/usr/bin/python3
"""
    Creates the State "California" with the City "San Francisco"
    in the database
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

    # Create all tables defined in Base
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create State "California"
        california = State(name="California")

        # Create City "San Francisco"
        san_francisco = City(name="San Francisco", state=california)

        # Add State and City objects to the session
        session.add(california)
        session.add(san_francisco)

        # Commit the session to save changes to the database
        session.commit()

    except Exception as e:
        # Rollback the session in case of error
        session.rollback()
        print("Error:", e)

    finally:
        # Close the session
        session.close()
