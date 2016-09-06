import unittest

from pack import Pack

class TestPack(unittest.TestCase):
    def setUp(self):
        self.pack = Pack()

    def test_get_card(self):
        self.assertIsNotNone(self.pack.get_card())

    def test_get_card_twice(self):
        self.assertNotEqual(self.pack.get_card(), self.pack.get_card())
