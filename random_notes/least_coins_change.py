money_amount = (float(input("How much money do you have? $")))
print("You have $"+str(money_amount))

quarters = 25
dimes = 10
nickles = 5
pennies = 1

"""I think I need to divide the number entered by the user by each coin value, store that value in a variable and
and then proceed with the rest of the coins with the remaining money.
I need to use modulo somewhere but not sure where just yet."""

calculations = money_amount % quarters

print(int(calculations))

print("This is the least number of coins it would take to equal the amount of money that you currently have:\n "+str())
