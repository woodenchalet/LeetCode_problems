import unittest

from merge_two_sorted_list import merge_two_list, ListNode


class MergeTwoListTest(unittest.TestCase):
    def test_merge_two_list_test_case(self):
        l1 = self.list_to_linked_list_node([1, 2, 4])
        l2 = self.list_to_linked_list_node([1, 3, 4])
        expect = [1, 1, 2, 3, 4, 4]
        actual = self.linked_list_node_to_list(merge_two_list(l1, l2))

        self.assertEquals(expect, actual)

    def list_to_linked_list_node(self, input_list):
        input_list.reverse()
        current = dummy_head_one = ListNode(0)
        while input_list:
            current.next = ListNode(input_list.pop())
            current = current.next

        return dummy_head_one.next

    def linked_list_node_to_list(self, linked_list_node):
        current = linked_list_node
        result_list = []
        while current:
            result_list.append(current.val)
            current = current.next

        return result_list
