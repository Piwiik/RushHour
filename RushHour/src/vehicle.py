#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Uro Pierrick
#Ferdjani Luqman
#Devaux Manon
"""
:mod:`vehicle` module

:author: Uro Pierrick, Ferdjani Luqman, Devaux Manon

:date: 2017, october

A module for vehicle representations in a Rush Hour game

This module provides :

class Vehicle


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
        if type(orientation)==bool and type(name)==str and len(name)==1 and name in "ABCDEFJKXZOPQR":
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
        :returns: the size of the vehicle
        :rtype: int
        """
        return self.__size

    def get_orientation(self):
        """
        :returns: True if the vehicle is vertical, False otherwise
        :rtype: bool
        """
        return self.__orientation

    def get_name(self):
        """
        :returns: the name of the vehicle
        :rtype: str
        """
        return self.__name

    def __eq__(self,other):
        """

        """
        try :
            return self.__name==other.__name and self.__orientation==other.__orientation
        except AttributeError :
            return False
