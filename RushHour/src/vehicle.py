#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Uro Pierrick
#Ferdjani Luqman
#Devaux Manon
"""
:mod:`vehicle` module

:author: `Uro Pierrick, Ferdjani Luqman, Devaux Manon`

:date: 2017, october
:last revision: 2017, december

A module for vehicle representations in a Rush Hour game

:Provides:

* class Vehicle

and methods

* `get_size`
* `get_orientation`
* `get_name`
* `__eq__`
* `__str__`

:Examples:

>>> vehicle1 = Vehicle(True, "A")
>>> vehicle2 = Vehicle(False, "O")
>>> vehicle1.get_size()
2
>>> vehicle2.get_size()
3
>>> vehicle1.get_orientation()
True
>>> vehicle2.get_orientation()
False
>>> vehicle1.get_name()
'A'
>>> vehicle2.get_name()
'O'
>>> vehicle1 == vehicle2
False
>>> vehicle1 == vehicle1
True
>>> vehicle1 == 1
False
>>> print(vehicle1)
Vehicle A of size 2 and positioned vertically.
"""

class VehicleError(Exception):
    pass

class Vehicle():
    __Allowed_names = [chr(ord("A")+i) for i in range(11)]+[chr(ord("O")+i) for i in range(4)]+["X"]+["Z"]

    def __init__(self,orientation,name) :
        """
        Initialization function for Vehicle class

        :param orientation: the orientation of the vehicle
            - True if the vehicle is vertical
            - False if the vehicle is horizontal
        :type orientation: bool
        :param name: the name of the vehicle
        :type name: str
        :returns: a Vehicle object corresponding to the parameters
        :rtype: Vehicle
        :UC: name is a letter between A and K or between O and R or Z or X
        """
        if type(orientation)==bool and type(name)==str and len(name)==1 and name in "ABCDEFGHIJKXZOPQR":
            self.__orientation = orientation
            self.__name = name
            if name in "OPQR" :
                self.__size = 3
            else :
                self.__size = 2
        else :
            raise VehicleError("Incorrect name or orientation for the initialization of the vehicle")

    def get_size(self):
        """
        return the size of the vehicle

        :returns: the size of self
        :rtype: int
        :UC: None
        :Example:

        >>> vehicle1 = Vehicle(True, "A")
        >>> vehicle1.get_size()
        2
        """
        return self.__size

    def get_orientation(self):
        """
        return True if the vehicle is vertical, False otherwise

        :returns: True if self is vertical, False otherwise
        :rtype: bool
        :UC: None
        :Example:

        >>> vehicle1 = Vehicle(True, "A")
        >>> vehicle1.get_orientation()
        True
        """
        return self.__orientation

    def get_name(self):
        """
        return the name of the vehicle

        :returns: the name of self
        :rtype: str
        :UC: None
        :Example:

        >>> vehicle1 = Vehicle(True, "A")
        >>> vehicle1.get_name()
        'A'
        """
        return self.__name

    def __eq__(self,other):
        """
        return True if the two objects are the same vehicle (if their name and orientation are the same), False otherwise

        :param other: the object tested
        :type other: any
        :returns: True if self and other are the same object with the same attributes
        :rtype: bool
        :UC: None
        :Example:

        >>> vehicle1 = Vehicle(True, "A")
        >>> vehicle2 = Vehicle(False, "O")
        >>> vehicle1 == vehicle1
        True
        """
        try :
            return self.__name==other.__name and self.__orientation==other.__orientation
        except AttributeError :
            return False

    def __str__(self):
        """
        return a string representation of the vehicle

        :returns: a string presenting the caracteristics of self
        :rtype: str
        :UC: None
        :Example:

        >>> vehicle1 = Vehicle(True, "A")
        >>> print(vehicle1)
        Vehicle A of size 2 and positioned vertically.
        """
        if self.__orientation :
            ori = "vertically"
        else :
            ori = "horizontally"
        return "Vehicle {} of size {} and positioned {}.".format(self.__name, self.__size, ori)

if __name__=="__main__":
    import doctest
    doctest.testmod()
