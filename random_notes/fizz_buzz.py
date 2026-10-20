"""This program cycles through the number between 1 and 100 then finds the numbers that are divisible by 3 and five and prints magic words next to those numbers.
This program is efficient because it solves the problem in fewer steps than a larger if elif statement."""
for i in range(1, 101): # cycling through the range of numbers
    print(i, end=" ") # prints the number in the range with an empty space at the end
    if i % 3 == 0: # checks whether the current number in the range is divisible by 3 to then trigger the following print statement
        print(end="abra")
    if i % 5 == 0: # checks whether the current number in the range is divisible by 5 to then trigger the following print statement
        print(end="cadabra")
    print()
