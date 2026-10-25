my_dict = {1:"One", 2:"Two", 3:"Three"}
for key in my_dict:
    print(str(key), str(my_dict[key]))

user_input = input("Enter a key to search for: ")
if user_input in my_dict:
    print("Found it!")