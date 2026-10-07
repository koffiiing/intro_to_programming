"""
Robert Fesperman
2026_10_07
player.py
"""

import random

def gen_name():
    first_syl = "Cam Jess Mag Cha Rob Brit Alex Thax".split()
    second_syl = "ron ca gie lie ert any der ton".split()
    first_piece = first_syl[random.randint(0, len(first_syl)-1)]
    second_piece = second_syl[random.randint(0, len(second_syl)-1)]
    return first_piece + second_piece

    # jobs = ["work as professor",
    # "rodeo clown during the great depression",
    # ""]
