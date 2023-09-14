#!/usr/bin/python3
"""DEFINE A NEW CLASS"""
from models.base import Base

class Rectangle(Base):
    """START A NEW RECTANGLE CLASS"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """INIT A NEW RECTANGLE
        ARGS
        ====
        width (int)
        height (int)
        x, y (int)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the value of the width"""
        return self.__width
    @width.setter
    def width(self, value):
        """set/update the width value"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Get the value of the height"""
        return self.__height
    @height.setter
    def height(self, value):
        """set/update the height value"""
        if type(value) != int:
             raise TypeError("height must be an integer")
         if value <= 0:
             raise ValueError("height must be >= 0")
         self.__height = value
    @property
    def x(self):
        """Get the value of the x"""
        return self.__x
    @x.setter
    def x(self, value):
        """set/update the x value"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    @property
    def y(self):
        """Get the value of the y"""
        return self.__y
    @y.setter
    def y(self, value):
        """set/update the y value"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height
    def display(self):
        """
        print in stdout the Rectangle instances with the character # -
        you don't nedd to handle x and y here
        """

