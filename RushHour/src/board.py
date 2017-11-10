#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Uro Pierrick
#Ferdjani Luqman
#Devaux Manon
"""
:mod:`board` module

:author: Uro Pierrick, Ferdjani Luqman, Devaux Manon

:date: 2017, october

A module for board representations in a Rush Hour game

This module uses from :mod:`vehicle`

class Vehicle

This module provides :

class Board


"""
from vehicle import *

class CollisionError(Exception):
    def __init__(self):
        self.message = "Two vehicles are occupying the same cell, which is forbidden"

class PositionError(Exception):
    def __init__(self):
        self.message = "A vehicle is out of the board, which is forbidden"

class NoVehicleError(Exception):
    def __init__(self):
        self.message = "No vehicle is present"

'''def is_accurate(description):
    """
    Used only once, when the game is first described by the user, to test if the description is of the right form or not
    """
    if type(description)==list and len(description)!=0 :
        for vehicle in description :
            try'''

class Board():
    def add_vehicle(self, vehicle, position, count=None):
        """
        :param vehicle: the vehicle you want to place
        :type vehicle: Vehicle
        :param position: the position of the vehicle in a 6*6 grid (from (0,0) to (5,5))
        :type position: tuple
        :param count:
        :UC: position is a couple of integers between 0 and 5
        """
        if count==None :
            count = vehicle.get_size()
        if count != 0 :
            count-=1
            try :
                if self.__cells[position]==None :
                    self.__cells[position]=vehicle
                    if vehicle.get_orientation():
                        self.add_vehicle(vehicle, (position[0]+1 , position[1]), count)
                    else :
                        self.add_vehicle(vehicle, (position[0] , position[1]+1), count)
                else :
                    print(vehicle.get_name(),"##", position)
                    raise CollisionError()
            except KeyError :
                raise PositionError()



    def __init__(self,vehicles):
        """
        Creates a board for a rush hour game of height and width 6 tiles

        :param vehicles: a list of tuples (name,size,orientation,position) where
            - orientation (bool) is the orientation of the vehicle (True for vertical, False for horizontal)
            - name (str) is the name of the vehicle (which is a name in the classic game)
            - position (tuple) is a tuple (x,y) of the position of the upmost and leftmost tile on which the vehicle rests
        :type vehicles: list
        :returns: a Board object corresponding to the parameters
        :rtype: Board
        :UC: vehicles describes accurately a valid board
        """
        self.__cells = dict([((x,y) , None) for x in range(6) for y in range(6)])
        for vehicle in vehicles :
            self.add_vehicle(Vehicle(vehicle[0],vehicle[1]), vehicle[2])

    def get_starting_cell(self,position):
        """
        If a vehicle lies on the cell of coordinates position, returns the coordinates of the cell which is the
        leftmost and upmost cell on which this vehicle lies
        If there is on vehicle, raises NoVehicleError

        :param position: the coordinates of the cell
        :type position: tuple
        :UC: position is a couple of integers between 0 and 5
        :returns: the coordinates of the cell as described above
        :rtype: tuple
        """
        if self.__cells[position]==None :
            raise NoVehicleError()
        elif self.__cells[position].get_orientation() :
            name = self.__cells[position].get_name()
            is_same = self.__cells[(position[0]-1 , position[1])].get_name()==name
            while position[0]!=0 and is_name :
                position = (position[0]-1 , position[1])
                is_same = self.__cells[(position[0]-1 , position[1])].get_name()==name

            return position
        else :
            name = self.__cells[position].get_name()
            try :
                is_same = self.__cells[(position[0] , position[1]-1)].get_name()==name
            except AttributeError :
                
            while position[1]!=0 and is_same :
                position = (position[0] , position[1]-1)
                is_same=self.__cells[(position[0] , position[1]-1)].get_name()==name
            return position

    def push_vehicle(self,direction,position):
        """
        Pushes the vehicle laying at the position of one cell in the direction direction
        If there is no vehicle there, raises NoVehicleError

        :param direction: If the vehicle is horizontal, True means right and False means left
            If the vehicle is vertical, True means down and False means up
        :type direction: bool
        :param position: coordinates of the cell on which lies the vehicle you want to move
        :type position: tuple
        :UC: position is a couple of integers between 0 and 5

        """
        size = self.__cells[position].get_size()
        if direction :
            if self.__cells[position].get_orientation():
                #vehicle is moving down
                try :
                    if self.__cells[(position[0]+size , position[1])] == None :
                        self.__cells[(position[0]+size , position[1])] = self.__cells[position]
                    else :
                        raise CollisionError()
                except KeyError :
                    raise PositionError()
            else :
                #vehicle is moving to the right
                try :
                    if self.__cells[(position[0] , position[1]+size)] == None :
                        self.__cells[(position[0] , position[1]+size)] = self.__cells[position]
                    else :
                        raise CollisionError()
                except KeyError :
                    raise PositionError()
            self.__cells[position]=None
        else :
            if self.__cells[position].get_orientation():
                #vehicle is moving up
                try :
                    if self.__cells[(position[0]-1 , position[1])] == None :
                        self.__cells[(position[0]-1 , position[1])] = self.__cells[position]
                    else :
                        raise CollisionError()
                    self.__cells[(position[0]+size-1 , position[1])]
                except KeyError :
                    raise PositionError()
            else :
                #vehicle is moving to the left
                try :
                    if self.__cells[(position[0] , position[1]-1)] == None :
                        self.__cells[(position[0] , position[1]-1)] = self.__cells[position]
                    else :
                        raise CollisionError()
                    self.__cells[(position[0] , position[1])+size-1]
                except KeyError :
                    raise PositionError()

    def get_possible_moves(self):
        """
        Computes the possible moves of a vehicle over one cell in the current board self
        :param self: a board
        :type self: Board
        :returns: a list of each move you can make in the form : (position,direction)
            where position (tuple) is a couple of integers which point to the starting cell of the vehicle
            and direction (bool) is the direction in which the vehicle can go, depending on its orientation
        :rtype: list
        :UC: none

        """
        res = list()
        starting_cells = []
        for i in range(6):
            for j in range(6):
                vehicle = self.__cells[(i,j)]
                if vehicle != None :
                    sc = self.get_starting_cell((i,j))
                    if sc not in starting_cells :
                        starting_cells.append(sc)
                        if vehicle.get_orientation():
                            #vehicle is vertical
                            try:
                                if self.__cells[(i-1,j)]==None :
                                    #can move downwards
                                    res.append(((i-1,j),False))
                            except KeyError :
                                pass
                            try:
                                if self.__cells[(i+1,j)]==None :
                                    #can move upwards
                                    res.append(((i+1,j),True))
                            except KeyError :
                                pass
                        else:
                            #vehicle is horizontal
                            try:
                                if self.__cells[(i,j-1)]==None :
                                    #can move to the left
                                    res.append(((i,j-1),False))
                            except KeyError :
                                pass
                            try:
                                if self.__cells[(i,j+1)]==None :
                                    #can move to the right
                                    res.append(((i,j+1),True))
                            except KeyError :
                                pass
        return res







    def __eq__(self,other):
        is_equal , i , j = True , 0 , 0
        while i<6 and is_equal :
            while j<6 and is_equal :
                is_equal = self.__cells[(i,j)]==other.__cells[(i,j)]
                j+=1
            j=0
            i+=1
        return is_equal

    def __repr__(self):
        """

        """
        print("#############")
        for x in range(6) :
            for y in range(6) :
                if self.__cells[(x,y)] == None:
                    name = " "
                else :
                    name = self.__cells[(x,y)].get_name()
                print("#"+name, end="")
            print("#")
        print("#############")

    def __str__(self):
        """
        """
        res = "#############\n"
        for x in range(6):
            for y in range(6):
                if self.__cells[(x,y)] == None:
                    res += "# "
                else :
                    res += "#"+self.__cells[(x,y)].get_name()
            res += "#\n"
        return res+"#############"
