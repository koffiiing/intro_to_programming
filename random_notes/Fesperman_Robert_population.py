"""
Robert Fesperman
2026_09_02
World Population Assignment
"""


def calc_area_per_person(area_sqmi, area_name):
    area_acres = area_sqmi * SQMI_TO_ACRE_CONV
    area_sqft = area_sqmi * SQMI_TO_SQFT_CONV #CAL TEXAS SQFT
    TX_ACRES_PER_PERSON = area_acres / WORLD_POP
    TX_SQMI_PER_PERSON = area_sqmi / WORLD_POP #CAL SQMI PER PERSON
    TX_SQFT_PER_PERSON = area_sqft / WORLD_POP # CAL SQFT PER PERSON
    print(area_name+": ")
    print("Acres per person: "+str(TX_ACRES_PER_PERSON))
    print("Square miles per person: "+str(TX_SQMI_PER_PERSON))#OUTPUT SQMI PER PERSON
    print("Square feet per person: "+str(TX_SQFT_PER_PERSON))#OUTPUT SQFT PER PERSON

WORLD_POP = 8_300_000_000
SQMI_TO_ACRE_CONV = 640
SQMI_TO_SQFT_CONV = 2.788e7

def main():
        print(f"""

        World population: {WORLD_POP}

        ~ This program will show the area per person if we take
        the entire world population and put it into one specific area. ~""")

        print("""
        Enter the letter that corresponds with the area you wish to view or enter 0 to quit :

        (T)exas
        (A)ustralia
        (G)eorgia
        """)

        user_input = input().upper()
        if user_input == "T":
            calc_area_per_person(261_232, "Texas")

        elif user_input == "A":
            calc_area_per_person(2_968_464, "Australia")

        elif user_input == "G":
            calc_area_per_person(57_906, "Georgia")

        else:
            print("Invalid selection.")

if __name__ == "__main__":
        main()
