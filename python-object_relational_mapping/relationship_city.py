#!/usr/bin/python3
"""Module that defines the City class used with relationship_state."""
from sqlalchemy import Column, ForeignKey, Integer, String
from relationship_state import Base


class City(Base):
    """Represent a city of the table cities.

    Attributes:
        id (int): auto-generated, unique, not null primary key.
        name (str): the name of the city, 128 characters at most.
        state_id (int): the id of the state of the city (states.id).
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True,
                unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
