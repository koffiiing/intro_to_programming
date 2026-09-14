"""
Robert Fesperman
2026_08_26
Basic Printing Practice
"""
import math
import random

#Get users integer. Convert to float from string because we need to do math with it.
user_int = float(input("Please enter an integer: "))
#Print sqrt of user INT. #I did not use AI for this. I know about the format "f" from the book I'm reading "Python Crash Course."
square_root_num = float(user_int)
result = math.sqrt(square_root_num)
print(f"The square root of the integer you entered is: {result}")

#Print the INT multiplied by pi.
multi_pi = user_int * math.pi
print(f"The product of the integer you entered multiplied by pi is {float(multi_pi)}")

#Print a few new lines.
print("\n\n")

#Ask user to enter their job
user_vocation = input("Where do you work dawg?! ")
#Print job they entered
print(f"Your profession is {user_vocation}! Very cool my dood!")

#Generate random number
ran_num = random.randint(1, 1000)
#Print random generated number as their lucky number
print(f"Your lucky number is {ran_num}!")

#Print a few new lines.
print("\n\n")

#Print name and major
print("Robert\tFesperman\tSoftware Development")
