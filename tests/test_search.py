import unittest

from algor.search import (
    binary_search,
    recur_binary_search,
    linear_search,
)


class TestSuit(unittest.TestCase):

    def test_binary_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, binary_search(array, 5))
        self.assertEqual(11, binary_search(array, 6))
        self.assertEqual(-1, binary_search(array, 7))
        self.assertEqual(-1, binary_search(array, -1))

    def test_recur_binary_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6]
        self.assertEqual(10, recur_binary_search(array, 5, 0, 11))
        self.assertEqual(11, recur_binary_search(array, 6, 0, 11))
        self.assertEqual(-1, recur_binary_search(array, 7, 0, 11))
        self.assertEqual(-1, recur_binary_search(array, -1, 0, 11))

    def test_liner_search(self):
        array = [1, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 6, 6, 6]
        self.assertEqual(6, linear_search(array, 4))
        self.assertEqual(10, linear_search(array, 5))
        self.assertEqual(-1, linear_search(array, 7))
        self.assertEqual(-1, linear_search(array, -1))


if __name__ == '__main__':
    unittest.main()
