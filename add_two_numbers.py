

def add_two_numbers_solution_one(num_one, num_two):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = []
    carry = 0
    while (num_one or num_two):
        current_num_one = 0 if num_one == [] else num_one.pop()
        current_num_two = 0 if num_two == [] else num_two.pop()

        current = carry + current_num_one + current_num_two
        carry = current / 10
        if current >= 10:
            current = current % 10

        result.append(current)

    if carry > 0:
        result.insert(0, 1)

    return result


def add_two_numbers(num_one, num_two):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    dummy_head = ListNode(0)
    carry = 0
    point_one = num_one 
    point_two = num_two
    current = dummy_head
    while point_one or point_two:
        point_one_value = 0 if not point_one else point_one.val
        point_two_value = 0 if not point_two else point_two.val
        total = carry + point_one_value + point_two_value
        current.next = ListNode(total % 10)
        current = current.next
        carry = total / 10
        point_one = None if not point_one else point_one.next
        point_two = None if not point_two else point_two.next

    if carry > 0:
        current.next = ListNode(1)

    return dummy_head.next



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
