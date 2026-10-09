"""
Robert Fesperman
2026_10_07
Game 1
"""

import player
import os
import subprocess

def main():

    while True:
        subprocess.run("cls" if os.name == "nt" else "clear", shell=True) # this clears the shell terminal each time a new name is generated
        print(f"\nPlayer name: {player.gen_name()}")

        print(f"\n{player.gen_history()}\n")

        user_input = input("Do you like this character (Y/N)?: ").upper()
        if user_input == "N":
            continue
        if user_input == "Y":
            break
        
if __name__ == "__main__":
    main()