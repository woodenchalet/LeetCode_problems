def binary_search(alist, item):
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last) / 2
        if alist[midpoint] == item:
            found = True
            break
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

a = [1, 3, 4, 6, 8]
print binary_search(a, 3)