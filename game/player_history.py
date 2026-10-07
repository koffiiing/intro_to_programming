"""
Robert Fesperman
2026_10_07
Player History
"""

import random

def gen_history():
    history = [
        "was a professional juggler in the circus.",
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
    return history[random.randint(0, len(history)-1)]