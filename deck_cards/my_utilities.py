"""
Brandon Walker
2026_09_21
my_utilities
"""

#d notation
#for example, 5d10 would be rolling a 10-sided die  5 times
#another example, 3d4 would be rolling a 4 sided die 3 times
#in other words, times d sides.

import random
import os
import subprocess

def clear_screen():
    command = "cls" if os.name == "nt" else "clear"
    subprocess.run(command, shell=True)

def roll_dice(times, sides):
    total = 0 #accumulator value
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total

def roll_target(times, sides):
    total = 0 #accumulator value
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total


def main():
    pass


if __name__ == "__main__":
    main()
