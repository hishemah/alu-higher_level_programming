#!/usr/bin/python3
"""List all City objects of the database hbtn_0e_14_usa, sorted by id.

Each line shows: <state name>: (<city id>) <city name>

Arguments: mysql username, mysql password, database name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    rows = session.query(State, City).filter(City.state_id == State.id)
    for state, city in rows.order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
