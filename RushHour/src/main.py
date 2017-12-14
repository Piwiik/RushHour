#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Uro Pierrick
#Ferdjani Luqman
#Devaux Manon
"""

:author: Uro Pierrick, Ferdjani Luqman, Devaux Manon

:date: 2017, november

The main module for Rush Hour solving

This module uses from :mod:`vehicle`

class Vehicle

This module uses from :mod:`board` :

class Board

"""
from board import *
from pickle import *

def get_input_initialization():
    """
    Returns a list usable for board.Board.__init__
    """
    remaining_names = "ABCDEFGHIJKXZOPQR"
    board = Board([])
    going_on = "Y"
    print("Please Begin adding vehicles :")
    print(board)
    while going_on=="Y" :
        JA = input("Name of the vehicle : (Possible names : {})\n".format(remaining_names)).upper()
        while len(JA)!=1 or not JA in remaining_names :
             print("Wrong name, please enter a new name.")
             JA = input("Name of the vehicle : (Possible names : {})\n".format(remaining_names)).upper
        remaining_names = remaining_names.replace(JA,"")
        OR = input("Orientation of the vehicle : (Possible orientations : (V)ertical or (H)orizontal\n").upper()
        while len(OR)!=1 or not OR in "VH" :
            print("Wrong orientation, please enter a new orientation.")
            OR = input("Orientation of the vehicle : (Possible orientations : (V)ertical or (H)orizontal\n").upper()
        POS1 = input("Vertical position of the vehicle : (From 0 on top row to 5 on bottom row)\n")
        while len(POS1)!=1 or POS1 not in "012345" :
            print("Wrong coordinate, please enter a new coordinate.")
            POS1 = input("Vertical position of the vehicle : (From 0 on top row to 5 on bottom row)\n")
        POS2 = input("Horizontal position of the vehicle : (From 0 on left column to 5 on right column)\n")
        while len(POS2)!=1 or POS2 not in "012345" :
            print("Wrong coordinate, please enter a new coordinate.")
            POS2 = input("Horizontal position of the vehicle : (From 0 on left row to 5 on right row)\n")
        try :
            board.add_vehicle(Vehicle(OR=="V",JA), (int(POS1),int(POS2)))
        except CollisionError :
            print("Your vehicle could not be placed because it is placed on another vehicle")
        except PositionError :
            print("Your vehicle could not be placed because it is placed partially out of the board")
        going_on = input("Would you like to add another vehicle ? (Y/N)").upper()
        while len(going_on)!=1 or not going_on in "YN" :
            print("Wrong input, please try again.")
            going_on = input("Would you like to add another vehicle ? (Y/N)").upper()
        if going_on=="N" :
            try :
                board.get_red_car()
            except NoRedCarError :
                print("No car is elligible as a red car.")
                print("Please add a new car that is placed horizontally on the third row.")
                going_on = "Y"
        print("The board now looks like this :")
        print(board)
    return board

def find_solution(board):
    try :
        solution = board.get_path()
        moves = solution.split("|")[:-1]
        print("Found a solution, press enter to view the next step")
        ah = input()
        for move in moves :
            board.push_vehicle( board.find_car(move[1]) , move[0] in "RD")
            print(board)
            ah = input()
        print("End of path.")
    except NoSolutionError :
        print("There is no solution for this board.")

def main():
    i=input("(T)extual or (G)raphical board solver? ")
    while len(i)!=1 or i.upper() not in "TG":
        print("Please enter a valid input.")
        i=input("(T)extual or (G)raphical board solver? ")
    if i.upper()=="T":
        find_solution(get_input_initialization())
    elif i.upper()=="G":
        print("Let's start by creating the board!")
        my_board=get_input_initialization()
        with open("my_board","wb") as f:
            p=Pickler(f)
            p.dump(my_board)
        import graphical
        graphical.main()

if __name__ == "__main__":
    main()
