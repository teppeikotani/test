import unittest
from compute import myadd


class TestMyAdd(unittest.TestCase):

    def test_add(self):
        val = myadd(1, 2)
        self.assertEqual(3, val)

    def test_add_pp(self):
        val = myadd(2, 6)
        self.assertTrue(val > 0)

    def test_add_nn(self):
        val = myadd(-2, -6)
        self.assertTrue(val < 0)


if __name__ == "__main__":
    unittest.main()
