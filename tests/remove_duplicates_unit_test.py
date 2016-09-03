import unittest

from remove_duplicates import remove_duplicates


class RemoveDuplicateTestCase(unittest.TestCase):
    def test_remove_duplicate(self):
        test_nums = [1, 1, 2]
        expect_result = [1, 2]
        self.assertEquals(expect_result, remove_duplicates(test_nums))
