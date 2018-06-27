def twoSum(nums, target):
    """
    :desc One-pass Hash Table
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    records = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in records:
            return [records[complement], index]
        records[num] = index
