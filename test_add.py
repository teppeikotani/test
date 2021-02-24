import unittest
from compute import myadd


class TestMyCompute(unittest.TestCase):

    def test_add(self):
        val = myadd(1, 2)
        self.assertEqual(3, val)


if __name__ == "__main__":
    unittest.main()
