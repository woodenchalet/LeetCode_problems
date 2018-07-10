import unittest

from add_two_numbers import add_two_numbers, add_two_numbers_solution_one, ListNode


class AddTwoNumbersListTest(unittest.TestCase):
    def test_add_two_numbers(self):
        num_one = [2, 4, 3]
        num_two = [5, 6, 4]

        expect_result = [7, 0, 8]
        self.assertEquals(
            expect_result, add_two_numbers_solution_one(num_one, num_two))


class AddTwoNumbersLinkedListNodeTest(unittest.TestCase):
    def test_add_two_numbers(self):
        num_one = self.list_to_linked_list_node([2, 4, 3])
        num_two = self.list_to_linked_list_node([5, 6, 4])
        expect_result = self.list_to_linked_list_node([7, 0, 8])

        self.assertEquals(
            self.linked_list_node_to_list(expect_result),
            self.linked_list_node_to_list(add_two_numbers(num_one, num_two)))

    def test_add_two_numbers_two(self):
        num_one = self.list_to_linked_list_node([1, 8])
        num_two = self.list_to_linked_list_node([0])
        expect_result = self.list_to_linked_list_node([1, 8])

        self.assertEquals(
            self.linked_list_node_to_list(expect_result),
            self.linked_list_node_to_list(add_two_numbers(num_one, num_two)))

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
