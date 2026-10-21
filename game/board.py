"""
Robert Fesperman
2026_10_21
Game Board
"""

def show_board(board):
    for row in board:
        print(" ".join(row))

board = [[".",".",".",".","."],
         [".",".",".",".","."],
         [".",".",".",".","."],
         [".",".",".",".","."]]

show_board(board)

# for postions use row/col instead of x/y
# code something to recall the current position of player
#
