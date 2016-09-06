import unittest

from pack import Pack

class TestPack(unittest.TestCase):
    def test_get_card(self):
        pack = Pack()
        self.assertIsNotNone(pack.get_card())
