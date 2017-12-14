#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Uro Pierrick
#Ferdjani Luqman
#Devaux Manon
"""

:author: Uro Pierrick, Ferdjani Luqman, Devaux Manon

:date: 2017, december

The graphical module for Rush Hour solving

This module uses from :mod:`vehicle`

class Vehicle

This module uses from :mod:`board` :

class Board

"""
from board import *
from tkinter import *
from pickle import *

fenetre = None
grid = None
gr_grid = []
tiles_bg_color={"Z":"#CB2700", "X":"#EB0B00", "A":"#8FD0A2", "B":"#F19717",
                "C":"#5D97F2", "D":"#EF7EAA", "E":"#6E41B2", "F":"#178B65",
                "G":"#3A4D50", "H":"#A9A77F", "I":"#DEFA4B", "J":"#765F4A",
                "K":"#416130", "O":"#E6C421", "P":"#B174BB", "Q":"#353EA4",
                "R":"#399C92" }

tiles_empty_bg="#9e948a"
tiles_font={"Verdana", 30, "bold"}
game_bg="#92877d"
game_size=600
tiles_size=game_size//6

with open("my_board","rb") as f:
    dp=Unpickler(f)
    my_board=dp.load()

def main():
    """
    Launch the graphical Rush Hour
    """
    global fenetre, gr_grid,grid,steps,btn
    fenetre = Frame()
    fenetre.grid()
    fenetre.master.title('Rush Hour')
    flabel = Frame(fenetre)
    flabel.grid()
    steps=StringVar()
    Label(flabel, textvariable=steps).pack()
    steps.set(str(len(l))+" steps remaining")
    background = Frame(fenetre, bg = game_bg, width=game_size, height=game_size)
    background.grid()
    gr_grid = []
    for i in range(6):
        gr_line = []
        for j in range(6):
            cell = Frame(background, bg = tiles_empty_bg, width = tiles_size, height = tiles_size)
            cell.grid(row=i, column=j,padx=1, pady=1)
            t = Label(master = cell, text = "", bg = tiles_empty_bg, justify = CENTER, font = tiles_font, width=4, height=2)
            t.grid()
            gr_line.append(t)
        gr_grid.append(gr_line)

    board_display(my_board)
    button=Frame(fenetre)
    button.grid()
    btn=StringVar()
    Button(button, textvariable=btn, command=next_step).pack(side=BOTTOM)
    btn.set("Next step")
    fenetre.mainloop()

def board_display(board):
    """
    Graphical board display
    """
    global gr_grid, fenetre
    for i in range(6):
        for j in range(6):
            if board.cells[(i,j)]==None:
                gr_grid[i][j].configure(bg=tiles_empty_bg,text="")
            else:
                value=board.cells[(i,j)].get_name()
                gr_grid[i][j].configure(bg=tiles_bg_color[value])
                pos=board.get_starting_cell((i,j))
                gr_grid[pos[0]][pos[1]].configure(text=value)
                if pos!=board.cells[(i,j)]:
                    gr_grid[i][j].configure(text="")

    fenetre.update_idletasks()

def board_solver(board):
    """
    Solve the board
    """
    solution=board.get_path()
    moves = solution.split("|")[:-1]
    l=[]
    for move in moves :
        tmp = board.copy()
        board = tmp.clone_and_push(board.find_car(move[1]), move[0] in "RD")
        l.append(board)
    return l

l=board_solver(my_board)

def next_step():
    """
    Events for the next step button
    """
    global fenetre, grid
    if len(l)>2:
        board_display(l[0])
        l.pop(0)
        steps.set(str(len(l))+" steps remaining")
    elif len(l)==2:
        board_display(l[0])
        l.pop(0)
        steps.set(str(len(l))+" step remaining")
    else:
        board_display(l[0])
        steps.set("No more steps remaining")
        btn.set("Finished!")

if __name__ == '__main__':
    main()
