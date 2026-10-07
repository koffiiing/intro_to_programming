"""
Robert Fesperman
2026_10_07
player.py
"""

import random

def gen_name():
    first_name = "Chud Nugget Magpie Monkey Trundle Smash Thimble Goose Pigeon Jelly Jigglewiggle".split()
    second_name = "Mackleson Anoos Blood Puncher Wigglebottom Thunderthighs O'Shenanigan O'Flander Dumper Thunderpants".split()
    third_name = ["Jr.", "Sr.", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    first_piece = first_name[random.randint(0, len(first_name)-1)]
    second_piece = second_name[random.randint(0, len(second_name)-1)]
    suffix = third_name[random.randint(0, len(third_name)-1)]
    return first_piece + " " + second_piece + " " + suffix

    # jobs = ["work as professor",
    # "rodeo clown during the great depression",
    # ""]
