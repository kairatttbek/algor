import unittest

from algor.sort import (
    insertion_sort,
)


class TestSuit(unittest.TestCase):

    def test_insertion_sort(self):
        self.assertEqual(
            [1, 5, 23, 57, 65, 1232],
            insertion_sort([1, 5, 65, 23, 57, 1232])
        )


if __name__ == '__main__':
    unittest.main()