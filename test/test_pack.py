import unittest

from pack import Pack

class TestPack(unittest.TestCase):
    def test_get_card(self):
        pack = Pack()
        self.assertIsNotNone(pack.get_card())

    def test_get_card_twice(self):
        pack = Pack()
        self.assertNotEqual(pack.get_card(), pack.get_card())
