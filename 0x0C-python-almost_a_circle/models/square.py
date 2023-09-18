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
        str_id = "({})".format(self.id)
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
        if args is not None and len(args) != 0:
            lst_atr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                if lst_atr[i] == 'size':
                    setattr(self, 'width', args[i])
                    setattr(self, 'height', args[i])
                else:
                    setattr(self, lst_atr[i],args[i])
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    setattr(self, 'width', value)
                    setattr(self, 'height', value)
                else:
                    setattr(self, key, value)
    def to_dictionary(self):
        """REPRESENTATION OF THE DIC"""
        lst_atr = ['id', 'size', 'x', 'y']
        dict_re = {}
        for key in lst_atr:
            if key == 'size':
                dict_re[key] = getattr(self, 'width')
            else:
                dict_re[key] = getattr(self, key)
        return dict_re
