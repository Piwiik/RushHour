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
    p = Pickler(ob_file)
    p.dump(board)
    ob_file.close()

def load_board():
    """
    Allows for a board from a previous game to be loaded if the user wishes to if no save file exists
    the user may input it by themselves
    """
    load = input("Would you rather (L)oad a file from a previous game, (C)reate your very own board, or (S)elect a board from the library ? (L/C/S) ").upper()
    while len(load)!=1 or load not in "LCS":
        print("Could not understand your input, please try again.")
        load = input("Would you rather (L)oad a file from your previous game, (C)reate your very own board, or (S)elect a board from the library ? (L/C/S) ").upper()
    if load=="L":
        try:
            ob_file = open("rushhour", "rb")
            p = Unpickler(ob_file)
        except IOError:
            choice = input("There is no save file, you may (C)reate your own game board or (S)elect a board from the library ")
            while len(choice)!=1 or choice.upper() not in "CS":
                print("Could not understand your input, please try again")
                choice = input("There is no save file, you may (C)reate your own game board or (S)elect a board from the library ")
            if choice.upper()=="C":
                return get_input_initialization()
            elif choice.upper()=="S":
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
        return p.load()
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
        vehicle_name = input("Choose one of the board's vehicles by name, enter 'exit' if you'd like to stop playing ")
        while not find_car(board,vehicle_name.upper()) and vehicle_name.lower()!="exit" :
            print("The vehicle you've chosen is not on the board")
            vehicle_name = input("Choose one of the board's vehicles by name ")
        if vehicle_name.lower()=="exit":
            quit="exit"
            save = input("Would you like to save your current progression ? (Y/N) Or would you like to see a (S)olution ")
            while len(save)!=1 or save.upper() not in "YNS":
                print("You may answer Y for yes, N for no or S if you'd like to see a solution, you may answer in lowercase if you wish")
                save = input("Would you like to save your current progression ? (Y/N) Or would you like to see a (S)olution ")
            if save.upper()=="Y":
                save_game(board)
            elif save.upper()=="S":
                find_solution(board)
        else:
            move = input("Choose in which direction you want the car to move (L,D,U,R) ")
            while len(move)!=1 or move.upper() not in "LDUR":
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


def main():
    j=input("""Welcome to the Rush Hour game interface you may choose between :
            - (S)olving automatically a specific set of your choosing (created or pre-made)
            - (P)laying the game with a specific set \n """)
    while len(j)!=1 or j.upper() not in "SP":
        print("Please enter a valid input")
        j=input("(S)olve automatically a set or (P)lay the game ?")
    if j.upper()=="S":
        i=input("(T)extual or (G)raphical board solver? ")
        while len(i)!=1 or i.upper() not in "TG":
            print("Please enter a valid input.")
            i=input("(T)extual or (G)raphical board solver? ")
        if i.upper()=="T":
            find_solution(load_board())
        elif i.upper()=="G":
            my_board=load_board()
            with open("my_board","wb") as f:
                p=Pickler(f)
                p.dump(my_board)
            import graphical
            graphical.main()
    elif j.upper()=="P":
        textual_game()

if __name__ == "__main__":
    main()
