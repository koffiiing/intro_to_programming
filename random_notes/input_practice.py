"""
Robert Fesperman
2026_08_31
Input Practice
"""

quaters = int(input("Enter the number of quarters: "))
dimes = int(input("Enter the number of dimes: "))
nickles = int(input("Enter the number of nickles: "))
pennies = int(input("Enter the dumber of pennies: "))

total = quaters * .25 + dimes * .10 + nickles * .05 + pennies * .01

print("Your total ammount of money is $"+str(total))

# Extra credit!
# Make a program that asks for a currency amount
# and then gives you the minimum number of coins for change
# For example, $1.78 would give you 7 Quaters and 3 pennies.
