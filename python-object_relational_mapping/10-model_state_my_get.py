#!/usr/bin/python3
"""Print the id of the State object whose name is given as argument.

"Not found" is printed when there is no such state. The name is passed
as a query parameter (safe from SQL injections).

Arguments: mysql username, mysql password, database name, state name
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session = sessionmaker(bind=engine)()
    state = session.query(State).filter(State.name == sys.argv[4]).first()
    if state is None:
        print("Not found")
    else:
        print(state.id)
    session.close()
