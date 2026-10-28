"""
Robert Fesperman
2026_10_07
Game 1
"""

import sys
import board
import my_utilities
import player
import board

def main():
    level = 1
    while True:

        my_utilities.clear_screen() # escape codes that clear the terminal each time a new player is generated

        new_player = player.gen_player(level) # calls gen_player to create a new player and assign it to new_player variable
        player.display_player(new_player)

        # Takes user imput to determine whether they are happy with the generated play. If they arent then a new player is generated.
        user_input = input("Do you like this character (Y/N)?: ").upper()
        if user_input == "N":
            continue
        if user_input == "Y":
            print("Good luck, " + new_player['name'] + "!")
            break

    # generates the game board and places player in random location it
    game_board = board.create_board()
    new_player = {'row': 0, 'col': 0}
    game_board, new_player = board.place_player(game_board, new_player)
    board.show_board(game_board)

if __name__ == "__main__":
    main()

"""
move player notes:
    main():
        # clear_screen
        # loop
        #   Player creation
        # create board
        # place player
        #
        # loop - main game loop
        #   show_board
        #   command player
"""

"""
command player notes
    command_player():
        command = get_command(board, player)
        board[player['row'][player['col']] = "."
        if command == "W":
            player['row'] -= 1
        elif for the other directions
        board[player['row'][player['col']] = "@"
        return board, player

        bone head way to deten

        if player row = 0:
            player['row']
            player['row'] = len(board) -1
        elif command == "Q":
        clear_screen()
            input("Thanks for playing!)
            sys.exit(0)

            something that he told us that is very useful in certain circumstances
"""
