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


# Rolls the dice and returns the total of all the rolls added together.
def roll_dice(times, sides):
    total = 0  # accumulator value
    for i in range(times):
        roll = random.randint(1, sides)
        total += roll
    return total


# Rolls the dice and returns how many rolls matched or beat the target.
def roll_target(times, sides, target):
    hits = 0  # counter for rolls that meet or beat the target
    for i in range(times):
        roll = random.randint(1, sides)
        if roll >= target:
            hits += 1
    return hits


# Extra credit: keeps asking until the user types only digits (0-9),
# then returns the answer as an int.
def get_whole_number(prompt):
    while True:
        user_input = input(prompt)
        is_valid = True
        if user_input == "":
            is_valid = False
        for letter in user_input:
            if letter < "0" or letter > "9":
                is_valid = False
        if is_valid:
            return int(user_input)
        print("Please enter a whole number using digits only.")


def main():
    print("\nWelcome to the Dice Roller!")
    print("You will choose how many dice to roll and how many sides each die has.")
    print("Then enter a target number:")
    print("  - Enter 0 for the target to get the TOTAL of all the dice.")
    print("  - Enter a number above 0 to count how many dice MATCHED or BEAT it.")
    print("Enter 0 for the number of rolls when you want to quit.")

    while True:
        roll_num = get_whole_number("Enter the number of times to roll (0 to quit): ")
        if roll_num == 0:
            print("Thanks for playing. Goodbye!")
            break

        side_num = get_whole_number("Enter the number of sides on the die: ")
        # Extra credit: sides cannot be 1 or less
        while side_num <= 1:
            print("A die must have at least 2 sides.")
            side_num = get_whole_number("Enter the number of sides on the die: ")

        target_num = get_whole_number("Enter a target number (0 for a total): ")

        if target_num == 0:
            result = roll_dice(roll_num, side_num)
            print("You rolled " + str(roll_num) + "d" + str(side_num)
                  + " for a total of " + str(result) + ".")
        else:
            result = roll_target(roll_num, side_num, target_num)
            print(str(result) + " out of " + str(roll_num)
                  + " dice matched or beat the target of " + str(target_num) + ".")
        print()


if __name__ == "__main__":
    main()
