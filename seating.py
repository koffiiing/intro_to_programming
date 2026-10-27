"""
Robert Fesperman
2026_10_26
Seating program
"""

import random

# creates the room
def create_room():
    room = []
    for i in range(5):
        row = []
        room.append(row)
        for j in range(5):
            row.append(".")
    return room

# prints room to terminal
def show_room(room):
    for row in room:
        print(" ".join(row))

# places student in available "seat" in room
def place_students(room, num_students):
    if num_students > len(room) * len(room[0]):
        print("Room too small!")
        return False
    for student_num in range(1, num_students+1):
        while True:
            row = random.randint(0, len(room)-1)
            col = random.randint(0, len(room[0])-1)
            if room[row][col] == ".":
                room[row][col] = str(student_num)
            break
    return room

def find_id(room_map, student_id):
    for row in room_map:
        if student_id in row:
            return True
    return False

def find_id_by_position(room_map, student_id):
    for row in range(len(room_map)):
        for col in range(len(room_map[row])):
            if room_map[row][col] == student_id:
                return (row, col)
    return False

def main():
    room = create_room()
    num_students = int(input("Enter the number of students to place: "))
    room_map = place_students(room, num_students)
    show_room(room_map)

    if room_map:
        student_id = (input("Enter the ID to find: "))
        if find_id(room_map, student_id):
            print("Found it!")

        position = find_id_by_position(room_map, student_id)
        if position:
            print(f"Number found at fow:{position[0]} col:{position[1]}")
        else:
            print("Number not in room map!")
    
if __name__ == "__main__":
    main()

# create function for moving students validate that desitnation is empty
# create a function for swapping students seats
# create a function for counting empty seats
#
