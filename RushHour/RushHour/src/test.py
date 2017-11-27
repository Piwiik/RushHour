#Fichier de test, à ignorer

from board import *
"""

vehicles = [(True,"A",(0,1)),(False,"B",(5,1)),(False,"Z",(2,0)),(True,"O",(0,5)),(True,"C",(4,0))]
board = Board(vehicles)
board2 = Board([(True,"A",(0,1)),(False,"B",(5,1)),(False,"X",(2,0)),(True,"O",(0,5)),(True,"C",(4,0))])


boards = dict([(board,"ah"),(board1,"beh"),(board2,"ces")])
"""
board1 = Board([(False,"H",(0,0)),(True,"O",(0,5)),(True,"P",(1,0)),(True,"Q",(1,3)),(False,"X",(2,1)),(True,"B",(4,0)),(False,"C",(4,4)),(False,"R",(5,2))])


print(board1)
copy = board1.copy()
print()
print(copy)
"""
board1.welcome_to_jurassic_park()
print(board1)

print(board1.get_possible_moves())


print(board.get_starting_cell((2,1)),"is the starting cell, expected (2, 0)")
print(board.get_starting_cell((2,5)),"is the starting cell, expected (0, 5)")
print(board.get_starting_cell((5,2)),"is the starting cell, expected (5, 1)")
print(board.get_starting_cell((5,5)),"is the starting cell, expected NoVehicleError")

vehicle1 = Vehicle(True,"A")
vehicle2 = Vehicle(False,"B")
vehicle3 = Vehicle(False,"Z")
vehicle4 = Vehicle(True,"O")

ah = [((x,y), "rero") for x in range(6) for y in range(6)]

beh = dict()

if (1,1) in beh :
    print("yeepee")
    """
