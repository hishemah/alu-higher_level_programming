#!/usr/bin/python3
"""Module that defines the State class with a relationship to its cities."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Represent a state of the table states.

    Attributes:
        id (int): auto-generated, unique, not null primary key.
        name (str): the name of the state, 128 characters at most.
        cities (list): the City objects of the state; they are deleted
            with the state.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")
