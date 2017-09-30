import random

from deuces import Card

NUMBERS = '23456789TJQKA'
SUITS = 'cdhs'
WHOLE_PACK = set([ Card.new(number + suit) for number in NUMBERS for suit in SUITS ])

class Pack():
    def __init__(self):
        self.shuffle()

    def get_card(self):
        card = random.choice(list(self.cards))
        self.cards.remove(card)
        return card

    def shuffle(self):
        self.cards = WHOLE_PACK.copy()
