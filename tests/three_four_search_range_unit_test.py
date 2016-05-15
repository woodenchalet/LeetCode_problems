import unittest

from three_four_search_range import search_range


class SearchRangeTestCase(unittest.TestCase):
    def test_search_range(self):
        test_list = [5, 7, 7, 8, 8, 10, 10, 10, 10, 10, 11, 21, 333]
        test_list_two = [1, 2, 3, 3, 3, 3, 4, 5, 9]
        self.assertEquals(search_range(test_list, 5), [0, 0])
        self.assertEquals(search_range(test_list, 7), [1, 2])
        self.assertEquals(search_range(test_list, 10), [5, 9])
        self.assertEquals(search_range(test_list, 12321), [-1, -1])
        self.assertEquals(search_range(test_list_two, 3), [2, 5])
