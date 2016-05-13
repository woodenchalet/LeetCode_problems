import unittest

from two_eight_three_move_zeros import move_zeroes


class MoveZeroesTestCase(unittest.TestCase):
    def test_move_zeroes(self):
        test_list_one = [1, 2, 3]
        test_list_two = [0]
        test_list_three = [1, 0, 3, 6, 0, 9, 0]
        test_list_four = [0, 0, 1]
        self.assertEquals(move_zeroes(test_list_one), [1, 2, 3])
        self.assertEquals(move_zeroes(test_list_two), [0])
        self.assertEquals(move_zeroes(test_list_three), [1, 3, 6, 9, 0, 0, 0])
        self.assertEquals(move_zeroes(test_list_four), [1, 0, 0])




