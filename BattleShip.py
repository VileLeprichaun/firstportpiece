# BattleShip
from random import randint
import os

board = []

for i in range(0,9):
    board.append(["0"]*9)
print(board)


#Board variables
max_rows = 9
max_column = 9 
num_ships = 4
max_ship_size = 5
min_ship_size = 2
