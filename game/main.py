"""
Robert Fesperman
2026_10_07
Game 1
"""

import board
import my_utilities
import player
import board

def main():
    level = 1
    while True:
        print("\033[H\033[2J\033[3J", end="") # escape codes that clear the terminal each time a new player is generated

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
