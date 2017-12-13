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

class NoRedCarError(Exception):
    def __init__(self):
        self.__message = "No vehicle can act as a red car"

class NoSolutionError(Exception):
    def __init__(self,message):
        self.__message = message

class IllegalMoveError(Exception):
    def init(self,message):
        self.__message = "This vehicle cannot be moved in this manner"

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
                if self.cells[position]==None :
                    self.cells[position]=vehicle
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

        :param vehicles: a list of tuples (orientation,name,position) where
            - orientation (bool) is the orientation of the vehicle (True for vertical, False for horizontal)
            - name (str) is the name of the vehicle (which is a name in the classic game)
            - position (tuple) is a tuple (x,y) of the position of the upmost and leftmost tile on which the vehicle rests
        :type vehicles: list
        :returns: a Board object corresponding to the parameters
        :rtype: Board
        :UC: vehicles describes accurately a valid board
        """
        self.cells = dict([((x,y) , None) for x in range(6) for y in range(6)])
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
        if self.cells[position]==None :
            raise NoVehicleError()
        elif self.cells[position].get_orientation() :
            #vehicle is vertical
            name = self.cells[position].get_name()
            try :
                is_same = self.cells[(position[0]-1 , position[1])].get_name()==name
                while position[0]!=0 and is_same :
                    position = (position[0]-1 , position[1])
                    is_same = self.cells[(position[0]-1 , position[1])].get_name()==name
            except AttributeError :
                pass
            except KeyError :
                pass
        else :
            #vehicle is horizontal
            name = self.cells[position].get_name()
            try :
                is_same = self.cells[(position[0] , position[1]-1)].get_name()==name
                while position[1]!=0 and is_same :
                    position = (position[0] , position[1]-1)
                    is_same=self.cells[(position[0] , position[1]-1)].get_name()==name
            except AttributeError :
                pass
            except KeyError :
                pass
        return position

    def push_vehicle(self,position,direction):
        """
        Pushes the vehicle laying at the position of one cell in the direction direction
        If there is no vehicle there, raises NoVehicleError

        :param position: coordinates of the cell on which lies the vehicle you want to move
        :type position: tuple
        :param direction: If the vehicle is horizontal, True means right and False means left
            If the vehicle is vertical, True means down and False means up
        :type direction: bool
        :UC: position is a couple of integers between 0 and 5
             position is the starting cell of a vehicle

        """
        size = self.cells[position].get_size()
        if direction :
            if self.cells[position].get_orientation():
                #vehicle is moving down
                try :
                    if self.cells[(position[0]+size , position[1])] == None :
                        self.cells[(position[0]+size , position[1])] = self.cells[position]
                    else :
                        raise CollisionError()
                except KeyError :
                    raise PositionError()
            else :
                #vehicle is moving to the right
                try :
                    if self.cells[(position[0] , position[1]+size)] == None :
                        self.cells[(position[0] , position[1]+size)] = self.cells[position]
                    else :
                        raise CollisionError()
                except KeyError :
                    raise PositionError()
            self.cells[position]=None
        else :
            if self.cells[position].get_orientation():
                #vehicle is moving up
                try :
                    if self.cells[(position[0]-1 , position[1])] == None :
                        self.cells[(position[0]-1 , position[1])] = self.cells[position]
                    else :
                        raise CollisionError()
                    self.cells[(position[0]+size-1 , position[1])] = None
                except KeyError :
                    raise PositionError()
            else :
                #vehicle is moving to the left
                try :
                    if self.cells[(position[0] , position[1]-1)] == None :
                        self.cells[(position[0] , position[1]-1)] = self.cells[position]
                    else :
                        raise CollisionError()
                    self.cells[(position[0] , position[1]+size-1)] = None
                except KeyError :
                    raise PositionError()

    def clone_and_push(self,position,direction):
        clone = self.copy()
        clone.push_vehicle(position,direction)
        return clone

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
        starting_cells = list()
        for i in range(6):
            for j in range(6):
                vehicle = self.cells[(i,j)]
                #print("testing",vehicle)
                if vehicle != None :
                    sc = self.get_starting_cell((i,j))
                    #print("found starting cell",sc)
                    if sc not in starting_cells :
                        #print("new starting cell")
                        starting_cells.append(sc)
                        if vehicle.get_orientation():
                            #print("vehicle is vertical")
                            try:
                                if self.cells[(i-1,j)]==None :
                                    #print("can move downwards")
                                    res.append((sc,False))
                            except KeyError :
                                pass
                            try:
                                if self.cells[(i+vehicle.get_size(),j)]==None :
                                    #print("can move upwards")
                                    res.append((sc,True))
                            except KeyError :
                                pass
                        else:
                            #print("vehicle is horizontal")
                            try:
                                if self.cells[(i,j-1)]==None :
                                    #print("can move to the left")
                                    res.append((sc,False))
                            except KeyError :
                                pass
                            try:
                                if self.cells[(i,j+vehicle.get_size())]==None :
                                    #print("can move to the right")
                                    res.append((sc,True))
                            except KeyError :
                                pass
        return res

    def find_car(self,name):
        """
        returns starting cell of the vehicle with the name name
        """
        for i in range(6) :
            for j in range(6) :
                if self.cells[i,j]!=None and self.cells[i,j].get_name()==name :
                    return (i,j)
        raise NoSolutionError("Couldn't find a vehicule with the name "+name)

    def get_red_car(self):
        """
        returns the name of the vehicle that will be considered as the "red car"
        which means that this vehicle will be the one the player has to move to the cell (2,5)
        the "red car" is the rightmost horizontal vehicle on the third line of the board
        """
        name = None
        for i in range(5) :
            vehicle = self.cells[(2,i)]
            if vehicle!=None and not vehicle.get_orientation() :
                name = vehicle.get_name()
        if name == None :
            raise NoRedCarError()
        else :
            return name

    def copy(self):
        """
        Copies self as a new board
        """
        clone = Board(list())
        clone.cells = self.cells.copy()
        return clone

    def __hash__(self):
        return hash(str(self))

    def __eq__(self,other):
        is_equal , i , j = True , 0 , 0
        while i<6 and is_equal :
            while j<6 and is_equal :
                is_equal = self.cells[(i,j)]==other.cells[(i,j)]
                j+=1
            j=0
            i+=1
        return is_equal

    def __repr__(self):
        """


        print("#0#1#2#3#4#5#")
        for x in range(6) :
            for y in range(6) :
                if self.cells[(x,y)] == None:
                    name = " "
                else :
                    name = self.cells[(x,y)].get_name()
                print("#"+name, end="")
            print("#")
        print("#0#1#2#3#4#5#")
        """
        res = "#0#1#2#3#4#5#\n"
        for x in range(6):
            for y in range(6):
                if self.cells[(x,y)] == None:
                    res += "# "
                else :
                    res += "#"+self.cells[(x,y)].get_name()
            res += "#\n"
        return res+"#0#1#2#3#4#5#"

    def __str__(self):
        """
        """
        res = "#0#1#2#3#4#5#\n"
        for x in range(6):
            for y in range(6):
                if self.cells[(x,y)] == None:
                    res += "# "
                else :
                    res += "#"+self.cells[(x,y)].get_name()
            res += "#\n"
        return res+"#0#1#2#3#4#5#"

    def Noirecommelechateauouflotteletendardnotredrapeau(self):
        """
        La force est noire
        """
        redcar = self.get_red_car()
        active_boards = set([(self,"")])
        farmed_boards = set([self])
        final_PATH = is_ended(active_boards,redcar)
        while final_PATH==None and len(active_boards)!=0 :
            active_boards = life_uh_finds_a_way(active_boards,farmed_boards)
            final_PATH = is_ended(active_boards,redcar)
        if len(active_boards)==0 :
            raise NoSolutionError("There is no solution to this problem")
        return final_PATH

def is_ended(boards,redcar) :
    """
    Returns the final board if the game is ended in one of the boards contained in the set boards, which means that the red car has reached the cell (2,5),
    otherwise returns None
    """
    for board in boards :
        if board[0].cells[(2,5)] != None and board[0].cells[(2,5)].get_name()==redcar :
            return board[1]
    return None

def life_uh_finds_a_way(active_boards,farmed_boards):
    """
    Jeff Eclosion d'Or
    returns a set of every possible board after every possible move from the set active_boards that are not already in the set farmed_boards
    Side effect : updates farmed_boards with the newly found boards
    """
    new_boards = set()
    for board in active_boards :
        moves = board[0].get_possible_moves()
        while moves!=list() :
            moved_board = move(board[0],moves)
            if not moved_board[0] in farmed_boards :
                new_boards.add((moved_board[0],board[1]+moved_board[1]))
                farmed_boards.add(moved_board[0])
    return new_boards

def move(board,moves):
    """
    Returns tuple containing a copy of board (a Board object) where the move indicated by the last tuple of moves has been done, and a letter indicating which move has been done
    L : Left ; R : Right ; U : Up ; D : Down
    Side effect : removes the tuple used from moves
    If moves is empty, raises assertion error
    """
    assert len(moves)!=0
    move = moves.pop()
    vehicle = board.cells[move[0]]
    if move[1] :
        if vehicle.get_orientation() :
            l = "D"
        else :
            l="R"
    else :
        if vehicle.get_orientation() :
            l = "U"
        else :
            l="L"
    return (board.clone_and_push(move[0],move[1]),l+vehicle.get_name()+"|")
