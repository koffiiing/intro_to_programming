"""
Robert Fesperman
2026_09_21
My Utilities
"""

# D notation
# for example, 5d10 would be rolling a 10-sided die 5 times.
# another example, 3d4 would be rolling a 4 sided die 3 times.
# in other words, times D sides.

import random

# If user target == 0 use this function.
def roll_dice(times, sides):
    total = 0 #accumulator value
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total

# need an if statement for assignment  to determine how many times the rolls hit the target number.



def main():
    pass

if __name__ == "__main__":
    main()
