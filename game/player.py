"""
Robert Fesperman
2026_10_07
player.py
"""

import random

def gen_name():
    """Generates a random name for the player by combining a first name, second name, and suffix."""
    first_name = "Chud Nugget Magpie Monkey Trundle Smash Thimble Goose Pigeon Jelly Jigglewiggle Steve Rick Rip Chugger Trunbutt".split() 
    second_name = "Mackleson Anoos Blood Puncher Wigglebothem Thunderthighs O'Shenanigan Flanders O'Flanegan Dumper Thunderpants".split()
    third_name = ["Jr.", "Sr.", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    first_piece = first_name[random.randint(0, len(first_name)-1)] # Taking a random name from the first_name list and assigning it to a variable
    second_piece = second_name[random.randint(0, len(second_name)-1)] # Doing the same thing here but from the second_name list
    suffix = third_name[random.randint(0, len(third_name)-1)] # ""
    return first_piece + " " + second_piece + " " + suffix # The end/output of the function which prints the three random names pulled from the three different lists

def gen_history():
    # list of origin stories for characters
    childhood = [
        "Your crap is all messed up and you talk funny.",
        "You were born a 19lb, 3oz baby and still are a 19lb, 3oz baby to this day. 37 years later. You're Still the same size and weight, execpt now you have telepathy powers and diabetes.",
        "You were born in the blood of your fathers enemies. Destined for glorious combat but you chose a different path and are far less cool now.",
     
    ]
    # list of character occupations
    occupation = [
        "You are now a plumber but a damn fine one. The best around.",
        "You are now an unemployed politcal protestor/aspiring social media influencer.",
        "You are now a famous explorer who hasn't yet discovered anything at all. At least you're famous though right?",
        "You are now a skilled musician who played in a world-famous orchestra.",
        "You are now a celebrated author of best-selling novels.",
        "You are now a legendary athlete who broke multiple records.",
        "You are now a legendary athlete who broke multiple records.",
        "You are now a brilliant scientist who made groundbreaking discoveries.",
        "You are now a talented artist whose paintings were displayed in galleries worldwide.",
        "You are now a successful entrepreneur who built a thriving business empire.",
        "You are now a respected politician who served their country with honor."
    ]

    first_hist = childhood[random.randint(0, len(childhood)-1)]
    second_hist = occupation[random.randint(0, len(occupation)-1)]
    history = first_hist + "\n\n" + second_hist
    return history


