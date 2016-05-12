import unittest

from three_longest_substring import length_of_longest_substring


class LengthOfLongestSubstringTestCase(unittest.TestCase):
    def test_answers(self):
        test_answer = 'abcabcbb'
        test_answer_two = 'bbbbb'
        test_answer_three = 'pwwkew'
        test_answer_four = 'c'
        test_answer_five = 'dvdf'
        test_answer_six = 'bpfbhmipx'
        self.assertEquals(length_of_longest_substring(test_answer), 3)
        self.assertEquals(length_of_longest_substring(test_answer_two), 1)
        self.assertEquals(length_of_longest_substring(test_answer_three), 3)
        self.assertEquals(length_of_longest_substring(test_answer_four), 1)
        self.assertEquals(length_of_longest_substring(test_answer_five), 3)
        self.assertEquals(length_of_longest_substring(test_answer_six), 7)
