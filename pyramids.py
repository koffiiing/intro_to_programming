"""
Robert Fesperman
2026_09_13
Great Pyramid Analysis
"""
import math

print("\n\n\t\t\t---- This program will show you some pretty interesting calculations related to the great pyramid! ----\n ")

print("""

Please select from the following:

Option A:

It has been estimated that the Great Pyramid of Giza weighs around 5.9 million tons.
It is also said that the pyramids only took 20 years to build.
Option A will calculate exactly how much stone would have had to have been moved each day to accomplish this seemingly impossible feet.

Option B:

Each side of the Great Pyramid is 230.4 meters and it's original height was 146.5m.
Option B will calculate the perimeter of the Great Pyramid, divide the perimeter by its height, and display the result.
Do you see a significance to this number?

Option C:



""")

# Variables used for calculations
days_in_20y = 20 * 365
stone_per_day = 5900000 / days_in_20y

while True:
    user_input = input("Please enter A, B, C (or enter Q to quit): ").upper()
    if user_input == "A":
        print(f"""

The ancient Egyptions would have had to move roughly {math.trunc(stone_per_day)} tons
or 17,000,000 pounds of stone per day to build the Great Pyramid of Giza in only 20 years.

""")

    elif user_input == "B":
        pass
    # do something
    elif user_input == "C":
        pass
    # do something
    elif user_input == "Q":
        break

#3
#
#
# Calc Circle 1 circumference
# side^2 + side^2 = C^2
# solve for c (squae root it)
# calculate circumference using c


# Calc circle 2 circumference


# Take circle 1 circumference and subract circle 2 circumference
