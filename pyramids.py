"""
Robert Fesperman
2026_09_13
Great Pyramid Analysis
"""

print("\n\n\t\t\t---- This program will show you some pretty interesting calculations related to the great pyramid! ----\n\n ")

print("""

Please select from the following: \n\nOption A: \n\n\tIt has been estimated that the Great Pyramid of Giza weighs around 5.9 million tons.
It is also said that the pyramids only took 20 years to build.\n\tOption A will calculate exactly how much stone was moved per day to accomplish this.
\n\nOption B,\n\nOption C\n

""")

stone_per_day = 5_900_000

while True:
    user_input = input("Please enter A, B, C (or enter Q to quit): ").upper()
    if user_input == "A":
        print(f"""\nThe ancient Egyptions would have had to move {stone_per_day} tons of stone per day to build the massive structure in only 20 years. """)
    # do something

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
