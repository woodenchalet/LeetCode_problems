def search_range(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index_start = -1
    index_end = -1
    index = 0
    found = False
    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = (first + last) / 2
        if nums[mid] == target:
            index = mid
            found = True
            break
        else:
            if target < nums[mid]:
                last = mid - 1
            else:
                first = mid + 1

    if not found:
        return [index_start, index_end]
    else:
        index_start = index
        index_end = index
        temp = index - 1
        while temp >= 0 and nums[temp] == target:
            index_start = temp
            temp -= 1

        temp = index + 1
        while temp < len(nums) and nums[temp] == target:
            index_end = temp
            temp += 1
    return [index_start, index_end]
