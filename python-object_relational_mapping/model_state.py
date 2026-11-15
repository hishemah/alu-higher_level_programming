#!/usr/bin/python3
"""Module that defines the State class and the Base of the SQLAlchemy models.

State is linked to the MySQL table states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represent a state of the table states.

    Attributes:
        id (int): auto-generated, unique, not null primary key.
        name (str): the name of the state, 128 characters at most.
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
