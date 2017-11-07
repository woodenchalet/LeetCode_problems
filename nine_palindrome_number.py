# Determine whether an integer is a palindrome. Do this without extra space.

def is_palindrome(num):
    """
    :type num: int
    :rtype: bool
    """
    if num < 0:
        return False 

    if num < 10:
        return True

    if num < 100:
        right = num/10
        left = num%10
        return right == left

    pivot = 10
    left = -1
    right = -1
    pivot_time = 1
    num_length = 0

    while right != 0:
        right = num/pivot
        left = num%pivot
        print('pivot: {pivot}, right:{right}, left:{left}'.format(pivot=pivot, right=right, left=left))
        if pivot > right:
            if right >= pivot/10:
                num_length = pivot_time * 2
                pivot /= 10
                for time in range(1,pivot_time+1):
                    print('pivot: {pivot}, right:{right}, left:{left}'.format(pivot=pivot, right=right/pivot, left=left% 10))
                    if right/pivot != left% 10:
                        return False
                    right %= pivot
                    left /= 10
                    pivot /= 10
            else:
                num_length = pivot_time * 2 -1
                pivot /= 10
                left %= pivot
                pivot /= 10
                for time in range(1,pivot_time):
                    print('pivot: {pivot}, right:{right}, left:{left}'.format(pivot=pivot, right=right/pivot, left=left% 10))
                    if right/pivot != left% 10:
                        return False
                    right %= pivot
                    left /= 10
                    pivot /= 10
        
            print(num_length)
            return True
        
        pivot *= 10
        pivot_time += 1

print(is_palindrome(123321))
