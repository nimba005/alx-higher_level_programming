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
        str_id = "({})".format(self.0x0C-python-almost_a_circleid)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_w = "{}/{}".format(self.width, self.height)
        return str_s + str_id + str_xy + str_w
    @property
    def size(self):
        """GET THE SIZE"""
        return self.width
    @size.setter
    def size(self, value):
        """UPDATE THE SIZE"""
        self.width = value
        self.height = value

    def __str__(self):
        """ STR DUNDER METHOD """
        str_rectangle = "[Squae]"
        str_id = "({})".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_size = "{}".format(self.size)
        return str_rectangle + str_id + str_xy + str_size
    def update(self, *args, **kwargs):
        """UPDATE THE SQUARE
        Args:
           *args (ints): New attribute value.
               - 1st argument representing id attribute
               - 2nd argument representing size attribute
               - 3rd argument representing x attribute
               - 4th argument representing y attribute
           **kwargs (dict): New key/value pairs of attributes
        """

