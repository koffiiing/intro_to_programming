"""
Robert Fesperman
2026_10_05
List Practice
"""

import random

#my_list = [0,1,2,3,4,5,6,7,8,9]
#print(my_list[0:4:2])

# The end of the list by twos
#my_list = [0,1,2,3,4,5,6,7,8,9]
#print(my_list[::2])

#my_list = [0,1,2,3,4,5,6,7,8,9]
#print(my_list[::-1])

# modifying the list *adding things to list
#my_list = [0,1,2,3,4,5,6,7,8,9]

#my_list[0] = 10

#print(my_list)



#my_list.append(10)

#print(my_list)

#my_list = [0,1,2,3,4,5,6,7,8,9]
#for num in my_list:
    #print(num, end = " ")
#print()

#user_num = int(input("Enter and integer: "))
#if user_num in my_list: # This is the search
    #print("Num in list!")
#else:
    #print("Num not found!")


#my_list = [0,1,2,3,4,5,6,7,8,9]
#my_list.insert(3, 10)
#print(my_list)

names = ["Rob", "Brandon", "Jason", "Steve", "Jacob"]

while True:
    position = random.randint(0,len(names)-1)
    print(names[position])
    input()

my_list = [0,1,2,3,4,5,6,7,8,9]
print(list(range(10)))
