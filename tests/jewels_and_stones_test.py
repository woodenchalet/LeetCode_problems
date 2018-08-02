import unittest

from jewels_and_stones import jewels_and_stones

class NumJwelesInStibesCase(unittest.TestCase):
    def test_num_jewels_in_stones(self):
        J = "aA"
        S = "aAAbbbb"
        expect_result = 3
        self.assertEquals(expect_result, jewels_and_stones(J, S))
