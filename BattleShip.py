# BattleShip
from random import randint
import os

board = []

for i in range(0,9):
    board.append(["0"]*9)

def print_board(board):
    for row in board:
        print (" ".join(row))

print_board(board)

def random_row(board):
    return randint(0, len(board)-1)
def random_col(board):
    return randint(0, len(board[0])-1)


ship_row = random_row(board)
ship_col = random_col(board)


guess_row =int()

guess_row = int()
#Board variables
max_rows = 9
max_column = 9 
num_ships = 4
max_ship_size = 5
min_ship_size = 2
