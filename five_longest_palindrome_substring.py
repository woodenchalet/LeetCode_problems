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

str = 'abba'
longest = ''
index = 0

if len(str) == 1:
    print str
else:
    for char in str:
        count = 0
        temp = ''
        if str[index - count] == str[index + count]:
            while index - count >= 0 and index + count < len(str) and str[index - count] == str[index + count]:
                if count == 0:
                    temp += char
                else:
                    temp = str[index - count] + temp + str[index + count]
                count += 1
        elif str[index - count] == str[index + count + 1]:
            while index + count + 1 < len(str) and index - count >= 0 and str[index - count] == str[index + count + 1]:
                temp = str[index - count] + temp + str[index + count + 1]
                count += 1
        else:
            continue

        if len(temp) > len(longest):
            longest = temp

        index += 1

    print longest
