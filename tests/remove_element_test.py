import unittest

from remove_element import remove_element


class RemoveElementTest(unittest.TestCase):
    def test_remove_element(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        expect_result = 5
        self.assertEquals(expect_result, remove_element(nums, val))
