"""
Robert Fesperman
2026_10_07
player.py
"""

import random

def gen_name():
    """Generates a random name for the player by combining a first name, second name, and suffix."""
    first_name = "Chud Nugget Magpie Monkey Trundle Smash Thimble Goose Pigeon Jelly Jigglewiggle Steve Rick Rip".split()
    second_name = "Mackleson Anoos Blood Puncher Wigglebottom Thunderthighs O'Shenanigan Flanders O'Flanegan Dumper Thunderpants".split()
    third_name = ["Jr.", "Sr.", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    first_piece = first_name[random.randint(0, len(first_name)-1)]
    second_piece = second_name[random.randint(0, len(second_name)-1)]
    suffix = third_name[random.randint(0, len(third_name)-1)]
    return first_piece + " " + second_piece + " " + suffix

def gen_history():

    childhood = [
        "Your crap is all messed up and you talk funny.",
        "was a renowned chef known for their unique recipes.",
        "was a famous explorer who discovered new lands.",
        "was a skilled musician who played in a world-famous orchestra.",
        "was a celebrated author of best-selling novels.",
        "was a legendary athlete who broke multiple records.",
        "was a brilliant scientist who made groundbreaking discoveries.",
        "was a talented artist whose paintings were displayed in galleries worldwide.",
        "was a successful entrepreneur who built a thriving business empire.",
        "was a respected politician who served their country with honor."
    ]

    occupation = [
        "You are a plumber but a damn fine one. The best around.",
        "You are an unemployed politcal protestor/aspiring social media influencer."
        ""
    ]

    first_hist = childhood[random.randint(0, len(childhood)-1)]
    second_hist = occupation[random.randint(0, len(occupation)-1)]
    history = first_hist + " \n\n" + second_hist
    return history


