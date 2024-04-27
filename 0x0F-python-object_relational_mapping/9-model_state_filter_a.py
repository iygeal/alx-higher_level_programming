#!/usr/bin/python3
"""Lists all State objects that contain the letter 'a'"""

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
        # Query State objects where name contains the letter 'a'
        states = session.query(State).filter(
            State.name.like('%a%')).order_by(State.id).all()

        # Print results
        for state in states:
            print(f"{state.id}: {state.name}")

    except Exception as e:
        print("Error:", e)

    finally:
        session.close()
