#!/usr/bin/python3

from sqlalchemy import Column, Integer, String, text
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declaractive_base
"""
    Creates a States class based on Base class.
"""
Base = declarative_base()

class States(Base):
    """
        our states class.
        Attribute: table name
        id: integer, unique Key
        name: String
        cities: Relationship with the other table
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all, delete-orphan",
        backref=backref("states", cascade="all"),
        single_parent=True)
