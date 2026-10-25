"""
Robert Fesperman
2026_10_21
Game Board
"""

import random

# for postions use row/col instead of x/y
# code something to recall the current position of player

def create_board():
    board = []
    for i in range(5):
        row = []
        board.append(row)
        for j in range(5):
            row.append(".")
    return board

def place_player(board, player):
    row = random.randint(0, len(board) -1)
    col = random.randint(0, len(board[0]) -1)
    player['row'] = row
    player['col'] = col
    board[row][col] = "@"
    return board, player

def show_board(board):
    for row in board:
        print(" ".join(row))



            
        