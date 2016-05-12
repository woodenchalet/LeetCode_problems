def length_of_longest_substring(given_string):
    """
    :type given_string: str
    :rtype: int
    """
    longest_length = 0
    temp = ''

    for char in given_string:
        if char not in temp:
            temp += char
        else:
            temp = temp[(temp.find(char)+1):] + char

        length = len(temp)
        if length > longest_length:
            longest_length = length

    return longest_length
