import unittest

from deuces import Card

from .holdem import count_outs

class TestCountOuts(unittest.TestCase):
    def test_simple(self):
        hand1 = [ Card.new(x) for x in ['Ac', 'Ad'] ]
        hand2 = [ Card.new(x) for x in ['5c', '7d'] ]
        turn = [ Card.new(x) for x in ['Ah', 'As', 'Ks', 'Qs'] ]
        self.assertEqual(count_outs(turn, hand1, hand2), (44, 0, 0))
