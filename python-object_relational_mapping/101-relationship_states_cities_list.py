#!/usr/bin/python3
"""List all State objects with their City objects, sorted by ids.

Arguments: mysql username, mysql password, database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda c: c.id):
            print("\t{}: {}".format(city.id, city.name))
    session.close()
