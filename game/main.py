"""
Robert Fesperman
2026_10_07
Game 1
"""

import player
import player_history
import os

def main():

    while True:

        print(f"\nPlayer name: {player.gen_name()}")

        print(f"\n{player_history.gen_history()}\n")

        user_input = input("Do you like this character (Y/N)?: ").upper()
        if user_input == "N":
            continue
        if user_input == "Y":
            break
        
if __name__ == "__main__":
    main()