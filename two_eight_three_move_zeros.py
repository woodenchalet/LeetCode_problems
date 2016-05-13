test_list = [0, 0, 1]


def move_zeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    num_of_zeros = 0
    for num in nums:
        if num == 0:
            num_of_zeros += 1

    for num in range(num_of_zeros):
        nums.remove(0)
        nums.append(0)

    print nums
    return nums


move_zeroes(test_list)
