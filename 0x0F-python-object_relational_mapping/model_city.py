#!/usr/bin/python3

"""
Class definition of a City
"""

from sqlalchemy import column, Integer, String, ForeignKey
from model_state import Base

class City(Base):
    """
    City class that inherits from Base
    Attributes:
        id: Id city
        name: Name of the city
        state_id: States id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
