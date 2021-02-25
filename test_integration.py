import unittest

# from compute import myadd, mymult
from unittest.mock import MagicMock
myadd = MagicMock()
mymult = MagicMock()

from integration import AddOrMult


def is_mock(obj):
    return obj.__class__.__name__ == 'MagicMock'


class TestAddOrMult(unittest.TestCase):

    def test_add(self):
        if is_mock(myadd):
            myadd.return_value = 8
        add_or_mult = AddOrMult(myadd, mymult)
        val = add_or_mult.do(2, 6, 'add')
        self.assertEqual(8, val)

    def test_mult(self):
        if is_mock(mymult):
            mymult.return_value = 12
        add_or_mult = AddOrMult(myadd, mymult)
        val = add_or_mult.do(2, 6, 'mult')
        self.assertEqual(12, val)


if __name__ == "__main__":
    unittest.main()
