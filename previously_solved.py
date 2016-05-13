def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for index, num in enumerate(nums):
        other_num = target - num
        for other_index, po_num in enumerate(nums):
            if other_num == po_num and index != other_index:
                return [index, other_index]


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    stack_one = []
    stack_two = []
    head_one = l1
    head_two = l2
    number_one = ''
    number_two = ''
    while head_one:
        stack_one.append(head_one.val)
        head_one = head_one.next

    while head_two:
        stack_two.append(head_two.val)
        head_two = head_two.next

    while stack_one:
        number_one += str(stack_one.pop())

    while stack_two:
        number_two += str(stack_two.pop())

    total = int(number_one) + int(number_two)
    str_total = str(total)
    stack_solution = []
    for char in str_total:
        stack_solution.append(ListNode(char))

    solution_node = stack_solution[-1]
    while stack_solution:
        current = stack_solution.pop()
        if stack_solution:
            current.next = stack_solution[-1]

    return solution_node


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
