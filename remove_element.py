def remove_element(nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    for i in range(nums.count(val)):
        nums.remove(val)
    
    return len(nums)
