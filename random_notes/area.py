"""
Robert Fesperman
2026_09_21
Area of Rhombus
"""

import math

"""
def calc_area_rhombus():
    p = int(input("Please enter horizantal measurment: "))
    q = int(input("Please enter vertical measurment: "))
    area = p * q / 2
    return area
"""



def calc_area_pentagon(a):
    result = 1/4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * a ** 2
    return result

print(calc_area_pentagon(10))

# PRACTICE BUILDING MATH FORMULAS AS FUNCTIONS




#def main():
