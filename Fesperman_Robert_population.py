"""
Robert Fesperman
2026_09_02
World Population Assignment
"""

WORLD_POP = 8_300_000_000
SQMI_TO_ACRE_CONV = 640
SQMI_TO_SQFT_CONV = 2.788e7

print("""

World population: 8,300,000,000

~ This program will show the area per person if we take
the entire world population and put it into one specific area. ~""")

print("""
Enter the letter that corresponds with the area you wish to view:

(T)exas
(A)ustralia
(G)eorgia
""")

user_input = input().upper()
if user_input == "T":
    TEXAS_SQMI = 261_232
    TEXAS_ACRES = TEXAS_SQMI * SQMI_TO_ACRE_CONV
    TEXAS_SQFT = TEXAS_SQMI * SQMI_TO_SQFT_CONV #CAL TEXAS SQFT
    TX_ACRES_PER_PERSON = TEXAS_ACRES / WORLD_POP
    TX_SQMI_PER_PERSON = TEXAS_SQMI / WORLD_POP #CAL SQMI PER PERSON
    TX_SQFT_PER_PERSON = TEXAS_SQFT / WORLD_POP # CAL SQFT PER PERSON
    print("Acres per person: "+str(TX_ACRES_PER_PERSON))
    print("Square miles per person: "+str(TX_SQMI_PER_PERSON))#OUTPUT SQMI PER PERSON
    print("Square feet per person: "+str(TX_SQFT_PER_PERSON))#OUTPUT SQFT PER PERSON

elif user_input == "A":
   AUS_SQMI = 2_968_464
   AUS_ACRES = AUS_SQMI * SQMI_TO_ACRE_CONV
   AUS_SQFT = AUS_SQMI * SQMI_TO_SQFT_CONV
   AUS_ACRES_PER_PERSON = AUS_ACRES / WORLD_POP
   AUS_SQMI_PER_PERSON = AUS_SQMI / WORLD_POP
   AUS_SQFT_PER_PERSON = AUS_SQFT /WORLD_POP
   print("Acres per person: "+str(AUS_ACRES_PER_PERSON))
   print("Square miles per person: "+str(AUS_SQMI_PER_PERSON))
   print("Square feet per person: "+str(AUS_SQFT_PER_PERSON))

elif user_input == "G":
   GA_SQMI = 57_906
   GA_ACRES = GA_SQMI * SQMI_TO_ACRE_CONV
   GA_SQFT = GA_SQMI * SQMI_TO_SQFT_CONV
   GA_ACRES_PER_PERSON = GA_ACRES / WORLD_POP
   GA_SQMI_PER_PERSON = GA_SQMI / WORLD_POP
   GA_SQFT_PER_PERSON = GA_SQFT / WORLD_POP
   print("Acres per person: "+str(GA_ACRES_PER_PERSON))
   print("Square miles per person: "+str(GA_SQMI_PER_PERSON))
   print("Square feet per person: "+str(GA_SQFT_PER_PERSON))

else:
   print("Invalid selection.")
