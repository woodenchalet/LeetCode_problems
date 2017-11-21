import sys
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """
    if n ==0:
        return
    index_nums1 = 0
    index_nums2 = 0
    for index in range(m, len(nums1)):
        nums1[index] = sys.maxint

    while index_nums1 < m+n:
        if nums1[index_nums1] < nums2[index_nums2]:
            index_nums1 +=1 
        else:
            nums1.insert(index_nums1, nums2[index_nums2])
            nums1.pop()
            index_nums1 += 1
            index_nums2 += 1
            if nums1[-1] != sys.maxint:
                return nums1
    
    return nums1

a = [-1,-1,0,0,0,0]
b = 4
c = [-1,0]
d = 2

print merge(a, b, c, d)