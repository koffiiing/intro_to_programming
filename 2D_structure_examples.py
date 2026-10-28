"""
Robert Fesperman
2026_10_21
2D structure example
"""

# system that allows the user to enter an employees information.
# this includes ID & name
# allow the user to keep entering employees until finished
# once finsihed, ask user for an ID.
#   #if ID in system, display the employee name
#   # otherwise, say not in system


employees = {}


while True:
    user_id = input("Enter ID# to add to system(-1 to quit): ")
    if user_id == "-1":
        break
    user_name = input("Enter the name associated with the ID: ")
    user_salary = input("Enter the salary accociated with that ID: ")
    employees[user_id] = {"name": user_name, 'salary':user_salary}

while True:
    user_id = input("Enter ID# to view employee(-1 to quit): ")
    if user_id == "-1":
        break
    if user_id in employees:
        print(employees[user_id]['name'])
        print(employees[user_id]['salary'])
    else:
        print("ID not in system.")
