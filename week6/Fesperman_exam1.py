"""
Robert Fesperman
2026_09_30
Exam 1
"""

import math

law_numbers = 5.67e-8
"""This program will calculate the luminosity of a star when provided the stars radius and temperature!
Enter 0 at any time to quit."""

def calc_lum(star_radius, star_temp):
    l = 4 * math.pi * star_radius ** 2 * 5.67e8 * star_temp ** 4
    return l


def main():
    while True:


        # Ask user for radius and temperature of a star
        star_radius = float(input("\nPlease enter the radius of a star in meters or enter 0 to quit: "))
        star_temp = float(input("Please enter the temperature of a star in kelvin: "))
        if star_radius == 0:
            break

            # I am melting right now. I have no idea why I can't remember how to do anything.
            # elif star_radius != "":
            # print("Invalid entry; please try again!")


        print(calc_lum(star_radius, star_temp))





if __name__ == "__main__":
    main()
