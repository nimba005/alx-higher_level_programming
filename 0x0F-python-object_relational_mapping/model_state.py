#!/usr/bin/python3

"""
Python file that contains the class definition of a State and a instance
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declaractive import declaractive_base

Base = declaractive_base()

class States(Base):
    """
    States class that inherits from Base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
