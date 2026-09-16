"""
Robert Fesperman
2026_09_13
Great Pyramid Analysis
"""
import math

print("\n\n\t\t\t---- THIS PROGRAM WILL SHOW YOU SOME INTERESTING CALCULATIONS RELATED TO THE GREAT PYRAMID OF GIZA!---- ")

print("""

Please select from the following:

Option A:

It has been estimated that the Great Pyramid of Giza weighs around 5.9 million tons.
It is also said that the pyramids only took 20 years to build.
Option A will calculate exactly how much stone the Egyptians would have had to move each day to accomplish this seemingly impossible feet.

Option B:

Each side of the Great Pyramid is 230.4 meters and it's original height was 146.5m.
Option B will calculate the perimeter of the Great Pyramid, divided by its height, and display the result.
Do you see a significance to this number?

Option C:

If we calculate the circumference

""")

# Calculation Variables
a_stones_per_day = 5900000 / (20 * 365)
b_cal = (230.4 * 4) / 146.5
# c1 = 230.4**2 + 230.4**2 = d**2
c2 = math.pi * 230.4 # I know this is only part of the equation. This is just for testing syntax.

while True:
    user_input = input("Please enter A, B, C (or enter Q to quit): ").upper()
    if user_input == "A":
        print(f"""

The ancient Egyptions would have had to move roughly {math.trunc(a_stones_per_day)} tons
or 17,000,000 pounds of stone per day to build the Great Pyramid of Giza in only 20 years.

""")

    elif user_input == "B":
        print(f"""

The output equals {b_cal}, which is an aproximation to Tau or 2pi.
This is significant because mathematical theorists highlight variations of measurements (including the 6.290 figure)
to suggest that the pyramid was deliberately built as a scale model to encapsulate the mathematical relationships of a sphere, specifically matching the proportions of the Earth

""")

    elif user_input == "C":
        print(c2)

    elif user_input == "Q":
        break

#3
#
#
# Calc Circle 1 circumference
# side^2 + side^2 = C^2
c_squared = 230.4 ** 2 + 230.4 ** 2
# solve for c (squae root it)
c = math.sqrt(c_squared)
# calculate circumference using c


# Calc circle 2 circumference


# Take circle 1 circumference and subract circle 2 circumference
