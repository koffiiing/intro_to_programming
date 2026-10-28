"""
Robert Fesperman
2026_10_05
List Practice
"""

import random

"""
# Prints elements from list from 0-3 by 2's or in incriments of 2 as specified by the 2 step.
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[0:4:2])

# The end of the list by twos
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[::2])

# prints the list in reverse
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[::-1])

# modifying the list adding things to list
my_list = [0,1,2,3,4,5,6,7,8,9]
# adding an element to the list in the 0 position
my_list[0] = 10

print(my_list)


# adding the number 10 to the end of the list
my_list.append(10)

print(my_list)

# a for loop that goes through the list and prints all of the numbers in the list on the same line with a space between them
my_list = [0,1,2,3,4,5,6,7,8,9]
for num in my_list:
    print(num, end = " ")
print()

# asks a user for a number and then takes that number and compares it to my_list and tells the user whether the number is on the list or not.
user_num = int(input("Enter and integer: "))
if user_num in my_list: # This is the search
    print("Num in list!")
else:
    print("Num not found!")


# adds the number 10 to the list in the 3 position and then prints the new list value
my_list = [0,1,2,3,4,5,6,7,8,9]
my_list.insert(3, 10)
print(my_list)
"""

# This program cycles randomly through a list of names and prints them out.
names = ["Rob", "Brandon", "Jason", "Steve", "Jacob"]


while True:
    position = random.randint(0,len(names)-1) #This cycles through the list of names and picks a random name and then assigns that name to a variable
    print(names[position])
    input()
