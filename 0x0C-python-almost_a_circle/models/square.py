#!/usr/bin/python3
"""Define a square"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Init a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """Make a new square
        Arguments
        =============
        SIZE: int
        X: int
        Y: int
        ID: int
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """STR DUNDER METHOD"""
        str_s = "[squaee]"
        str_id = 
