"""
Robert Feperman
2026_09_16
Function Practice
"""

import math

def calc_circumference(radius):
    result = 2 * math.pi * radius
    return result

def main():
    side = 230.4
    print("Circumference of a circle enclosing the Great Pyramid is: ")
    print(calc_circumference(side))

main()
