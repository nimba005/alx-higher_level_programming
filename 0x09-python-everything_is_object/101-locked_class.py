#!/usr/bin/python3
"""This defines a locked class"""

class LockedClass:
    """
    Only allow instatiation of an attribute called dirst_name
    """
    __slots__ = ["first_name"]
