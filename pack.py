from deuces import Card

NUMBERS = '23456789TJQKA'
SUITS = 'cdhs'
WHOLE_PACK = set([ Card.new(number + suit) for number in NUMBERS for suit in SUITS ])

class Pack():
    def get_card(self):
        return Card.new('Ah')
