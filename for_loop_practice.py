"""
Robert Fesperman
2026_09_09
For Loop Practice
"""

# prints each letter in ABDCEF one at a time.
for letter in "ABCDEF":
    print(letter)

name = "Robert"
for i in name:
    print(i)

name = "Robert"
for i in name:
    print(i, end="\t")

count = 0
while count < 5:
    count += 1

for i in range(5):
    print(i)

for i in range(1,11):
    print(i)
# prints 1-21 by 2's. Utilizes the "step" feature or function
for i in range(1, 22, 2):
    print(i)

for i in range (10):
    if i % 2 == 0:
        continue
    print(i)

for i in "Brandon":
    if i == "n":
        continue
    print(i)

# Compound Conditions
if first_name = "brandon" and last_name == "Walker":
    # checks for both firsName and lastName
while health > 0 or user_input != "Q":
    # continues to loop as long as the user does not
    # enter "Q or their heath remains above 0"

# While loop
while True:
    user_input = input("Enter password: ")
    if user_input == "password":
        break

# For loop

for letter in "Brandon":
    print(letter)
