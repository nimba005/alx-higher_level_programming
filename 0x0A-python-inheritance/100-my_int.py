#!/usr/bin/python3
"""This module defines a class MyInt that inherits from int"""

class MyInt(int):
    """Inverts int operators == and !="""

    def __eq__(self, value):
        """Overide == operator with != behavior"""
        return self.real != value
    def __ne__(self, value):
        """Overide != operator with == behavior"""
        return self.real == value
