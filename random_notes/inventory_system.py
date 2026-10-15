"""
Robert Fesperman
2026_10_14
Inventory System
"""

def view_inventory(inventory):
    for key in inventory:
        print(str(key), str(inventory[key]))

def add_item(inventory):
    # ask user for an item to add
    # check if item is in dictionary
    # if it is, incremenet value by 1
    # if not, add to dictionary with a valye of 1
    # do not add empty item
    item = input("Enter an item to add: ").strip().title()
    if item == "":
        return inventory
    elif item in inventory:
        inventory[item] += 1
    else:
        inventory[item] = 1
    return inventory

def use_item(inventory):
    # ask for an item
    # if item is in inventory, decerement bu one
    # if not, tell them item is not in inventory
    # if this is the last one, remove key entirely
    item = input("Enter item to use: ").strip().title()
    if item == "":
        return inventory
    value = inventory.get(item)
    if value is None:
        print("Item is not inventory")
    elif inventory[item] > 1:
        inventory[item] -= 1
    else:
        del inventory[item]
    return inventory

def drop_item(inventory):
   item = input("Enter an item you wish to drop all of: ").strip().title()
   if item == "":
     return inventory
   elif item not in inventory:
     print("Item not in inventory")
   else:
     del inventory[item]
     return inventory

def main():
    inventory = {
        "Potion":5,
        "Sword":1,
        "Shield":1,
        "Arrows":40
}

    while True:
        print("___INVENTORY MENU___")
        print("1. View inventory")
        print("2. Add an item: ")
        print("3. Enter an item to use: ")
        print("4. Drop all of an item: ")
        print("Enter Q to quit".upper())
        user_choice = input("Choice?: ").upper()
        if user_choice == "1":
            view_inventory(inventory)
        elif user_choice == "2":
            add_item(inventory)
        elif user_choice == "3":
            use_item(inventory)
        elif user_choice == "4":
            drop_item(inventory)
        elif user_choice == "Q":
            break

if __name__ == "__main__":
    main()
