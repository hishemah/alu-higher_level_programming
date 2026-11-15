#!/usr/bin/python3
"""Create the State California with the City San Francisco.

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
    Base.metadata.create_all(engine)
    state = State(name="California")
    state.cities.append(City(name="San Francisco"))
    session.add(state)
    session.commit()
    session.close()
