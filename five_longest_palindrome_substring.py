# str = "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddd" \
#       "ddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd"

str = 'babad'
longest = ''
index = 0

if len(str) == 1:
    print str
else:
    for char in str:
        count = 0
        temp_odd = char
        temp_even = char
        temp = ''

        while index + count + 1 < len(str) and index - count >= 0 \
                and str[index - count] == str[index + count + 1]:
            # abba
            if count == 0:
                temp_even += char
            else:
                temp_even = str[index - count] + temp_even + str[index + count + 1]
            count += 1

        count = 0
        while index - count - 1 >= 0 and index + count + 1 < len(str) \
                and str[index - count - 1] == str[index + count + 1]:
            # aba
            temp_odd = str[index - count - 1] + temp_odd + str[index + count + 1]
            count += 1

        index += 1
        if len(temp_odd) > len(temp_even):
            temp = temp_odd
        else:
            temp = temp_even

        if len(temp) > len(longest):
            longest = temp

    print longest
