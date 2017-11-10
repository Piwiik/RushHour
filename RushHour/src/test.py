from board import *

vehicle1 = Vehicle(True,"A")
vehicle2 = Vehicle(False,"B")
vehicle3 = Vehicle(False,"Z")
vehicle4 = Vehicle(True,"O")

vehicles = [(True,"A",(0,1)),(False,"B",(5,1)),(False,"Z",(2,0)),(True,"O",(0,5)),(True,"C",(4,0))]
board = Board(vehicles)
print(board)

print(board.get_starting_cell((2,1)),"is the starting cell")
print(board.get_starting_cell((2,5)),"is the starting cell")
print(board.get_starting_cell((5,2)),"is the starting cell")
print(board.get_starting_cell((5,5)),"is the starting cell")

"""
ah = [((x,y), "rero") for x in range(6) for y in range(6)]

beh = dict(ah)
"""
