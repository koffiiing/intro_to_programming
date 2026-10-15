"""
Robert Fesperman
2026_09_16
Slot Machine
"""
import random

bank_roll = 100

# Put money machine
user_bet = int(input("Enter a bet: "))

for i in range(3):
# Generate random slot image
# TODO: How to retreive three images for payout? How do we identify winnings.
    slot1 = random.randint(1,5)
    if slot1 == 1:
        print("Lemon")
    elif slot1 == 2:
        print("Melon")
    elif slot1 == 3:
        print("Bar")
    elif slot1 == 4:
        print("7")
    elif slot1 == 5:
        print("Cherry")
