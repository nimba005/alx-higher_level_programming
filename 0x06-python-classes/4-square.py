#!/bin/bash/python3

class Square:
    def __init__(self, size=0) -> None:
        self.size = size
    @property
    def size(self):
        """ Gets the attributes to be used in class """
        return self.__size
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """ Compares area of a square """
        return self.__size ** 2
