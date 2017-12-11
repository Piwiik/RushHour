#Fichier de test, à ignorer

from board import *
from timeit import timeit
"""

vehicles = [(True,"A",(0,1)),(False,"B",(5,1)),(False,"Z",(2,0)),(True,"O",(0,5)),(True,"C",(4,0))]
board = Board(vehicles)
board1 = Board([(False,"H",(0,0)),(True,"O",(0,5)),(True,"P",(1,0)),(True,"Q",(1,3)),(False,"X",(2,1)),(True,"B",(4,0)),(False,"C",(4,4)),(False,"R",(5,2))])


boards = dict([(board,"ah"),(board1,"beh"),(board2,"ces")])
print("copy took {} seconds for the test".format(timeit(stmt='board1.copy()',setup='from board import Board ; board1 = Board([(False,"H",(0,0)),(True,"O",(0,5)),(True,"P",(1,0)),(True,"Q",(1,3)),(False,"X",(2,1)),(True,"B",(4,0)),(False,"C",(4,4)),(False,"R",(5,2))])')))

"""

board1 = Board([(True,"A",(0,1)),(False,"B",(5,1)),(False,"X",(2,0)),(True,"O",(0,5)),(True,"C",(4,0))])
print(board1)
print("PATHAUXMAISPAVRAINONPLUS")
ah = board1.Noirecommelechateauouflotteletendardnotredrapeau()
for board in ah :
    print(board,"\n")
"""
print(board1)

print(board1)
board = board1.clone_and_push((0,0),True)
print()
print(board)
board1.welcome_to_jurassic_park()

print(board1.get_possible_moves()
"""
