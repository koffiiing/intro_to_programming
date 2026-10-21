"""
Robert Fesperman
2026_10_21
Deck of Cards
"""
import random
import my_utilities


def build_deck():
    deck = []
    suits = "Hearts Clubs Diamonds Spades".split()
    ranks = "2 3 4 5 6 7 8 9 10 Jack Queen King Ace".split()
    for suit in suits:
        for rank in ranks:
            card = {'rank':rank, 'suit':suit}
            deck.append(card)
    return deck

def shuffle_deck(deck):
    for i in range(10000):
        pos1 = random.randint(0, len(deck)-1)
        pos2 = random.randint(0, len(deck)-1)
        temp = deck[pos1]
        deck[pos1] = deck[pos2]
        deck[pos2] = temp
    return deck

def fisher_yates_shuffle_deck(deck):
    for i in range(len(deck)-1, 0, -1):
        j = random.randint(0,i)
        deck[i], deck[j] = deck[j], deck[i]
    return deck

def display_card(card):
    return card['rank'] + " of " + card['suit']

def draw_card(deck):
    if len(deck) == 0:
        deck = build_deck()
        deck = fisher_yates_shuffle_deck(deck)
    return deck.pop()

def main():
    deck = build_deck()
    deck = fisher_yates_shuffle_deck(deck)
    while True:
        card = draw_card(deck)
        input(display_card(card))
    

if __name__ == "__main__":
    main()



