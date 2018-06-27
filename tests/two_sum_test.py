import unittest

from two_sum import twoSum

class twoSumTestCase(unittest.TestCase):
    def test_two_sum(self):
        nums = [2, 7, 11, 15]
        target = 9
        expect_result = [0, 1]
        self.assertEquals(expect_result, twoSum(nums, target))
