#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Uro Pierrick
#Ferdjani Luqman
#Devaux Manon
"""

:author: Uro Pierrick, Ferdjani Luqman, Devaux Manon

:date: 2017, december

The main module for playing Rush Hour

This module uses from :mod:`vehicle`

class Vehicle

This module uses from :mod:`board` :

class Board

"""

from board import *
from main import *
import pickle

def input_move(board,move,vehicle_name):
    """
    Takes a move and car input by the user, and moves the vehicle in the desired direction

    :param move: Direction in which the vehicle must be moved (L,R,U,D)
    :type move: str

    :param board: A board of vehicles
    :type boards: Board

    :param vehicle_name: A vehicle's name
    :type vehicle_name: str

    :returns: new modified board with the move made
    :rtype: Board

    """
    position = board.find_car(vehicle_name)
    vehicle = board.cells[position]
    if move=="L":
        if vehicle.get_orientation():
            raise IllegalMoveError("The vehicle cannot be moved in such manner")
        else:
            direction = False
            new_board = board.clone_and_push(position, direction)
    elif move=="R":
        if vehicle.get_orientation():
            raise IllegalMoveError("The vehicle cannot be moved in such manner")
        else:
            direction = True
            new_board = board.clone_and_push(position, direction)
    elif move=="U":
        if not vehicle.get_orientation():
            raise IllegalMoveError("The vehicle cannot be moved in such manner")
        else:
            direction = False
            new_board = board.clone_and_push(position, direction)
    else:
        if not vehicle.get_orientation():
            raise IllegalMoveError("The vehicle cannot be moved in such manner")
        else:
            direction = True
            new_board = board.clone_and_push(position, direction)
    return new_board

def is_game_ended(board,redcar) :
    """
    Returns True if the game is ended which means that the red car has reached the cell (2,5), False otherwise.
    """
    if board.cells[(2,5)] != None and board.cells[(2,5)].get_name()==redcar :
        return True
    return False

def find_car(board,name):
    """
    returns True if the car is found and False otherwise
    """
    found_car = False
    i=0
    j=0
    while i<6:
        while j<6 and not found_car:
            if board.cells[i,j]!=None and board.cells[i,j].get_name()==name :
                found_car = True
            j+=1
        j=0
        i+=1
    return found_car

def save_game(board):
    """
    Allows to save a board in a binary file that can be later read and loaded
    to resume game
    """
    ob_file = open("rushhour", "wb")
    pickle.dump(board, ob_file)
    ob_file.close()

def load_board():
    """
    Allows for a board from a previous game to be loaded if the user wishes to if no save file exists
    the user may input it by themselves
    """
    load = input("Would you rather (L)oad a file from your previous game, (C)reate your very own board, or (S)elect a board from the library ? (L/C/S) ").upper()
    while load not in "LCS":
        print("Could not understand your input, please try again.")
        load = input("Would you rather (L)oad a file from your previous game, (C)reate your very own board, or (S)elect a board from the library ? (L/C/S) ").upper()
    if load=="L":
        try:
            ob_file = open("rushhour", "rb")
        except IOError:
            print("There is no save file, you may build your own game board")
            return get_input_initialization()
        return pickle.load(ob_file)
    elif load=="C":
        print("You may build your very own board to play with ")
        return get_input_initialization()
    else :
        from boards import BOARDS
        difficulty = input("Please choose a difficulty : (B)eginner (I)ntermediate (A)dvanced (E)xpert  ").upper()
        while difficulty not in "BIAE" :
            print("Could not understand your input, please try again.")
            difficulty = input("Please choose a difficulty : (B)eginner (I)ntermediate (A)dvanced (E)xpert  ").upper()
        print("You may choose between those boards :")
        d = ["BEGINNER","INTERMEDIATE","ADVANCED","EXPERT"]["BIAE".find(difficulty)]
        for i in range(1,11) :
            print("Board n°"+str(i))
            print(BOARDS[d+str(i)])
        choice = input("Which board will you choose ? (1 to 10)  ")
        while int(choice) not in range(1,11) :
            print("Could not understand your input, please try again.")
            choice = input("Which board will you choose ? (1 to 10)  ")
        return BOARDS[d+choice]

def textual_game():
    """
    Function that allows for a game of Rushhour to be played
    """
    board = load_board()
    print("You chose this board :")
    print(board)
    redcar = board.get_red_car()
    quit=None
    while not is_game_ended(board,redcar) and quit!="exit":
        vehicle_name = input("Choose one of the board's vehicles by name, or enter 'exit' if you'd like to stop playing ")
        while not find_car(board,vehicle_name.upper()) and vehicle_name.lower()!="exit" :
            print("The vehicle you've chosen is not on the board")
            vehicle_name = input("Choose one of the board's vehicles by name ")
        if vehicle_name.lower()=="exit":
            quit="exit"
            save = input("Would you like to save your current progression ? (Y/N) ").upper()
            while save not in "YN":
                print("You may answer Y for yes or N for no, you may answer in lowercase if you wish")
                save = input("Would you like to save your current progression ? (Y/N) ").upper()
            if save.upper()=="Y":
                save_game(board)
        else:
            move = input("Choose in which direction you want the car to move (L,D,U,R) ")
            while not move.upper() in "LDUR":
                print("You've chosen an invalid direction, choose either L(left), D(down), R(right) or U(up)")
                move = input("Choose in which direction you want the car to move (L,D,U or R) ")
            tmp = board.copy()
            try:
                board = input_move(tmp,move.upper(),vehicle_name.upper())
            except CollisionError:
                print("The move makes the vehicle collide with another one, choose another vehicle or/and move")
            except PositionError:
                print("The move puts a vehicle outside of the board's bounds, choose another vehicle or/and move")
            except IllegalMoveError:
                print("The move is impossible to do given the vehicle's orientation, choose another vehicle or/and move")
        print(board)
    if is_game_ended(board,redcar):
        print("Congratulations, you won !")

if __name__=='__main__':
    textual_game()
