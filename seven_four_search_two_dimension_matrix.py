def search_matrix(matrix, target):
    last_row = len(matrix) - 1
    last_column = len(matrix[0]) - 1
    first = 0
    found = False
    if target > matrix[last_row][last_column] or target < matrix[0][0]:
        return False

    while first <= last_row and not found:
        mid_point = int((first + last_row) / 2)
        if matrix[mid_point][0] == target:
            return True

        if target > matrix[mid_point][0]:
            if (mid_point + 1 <= len(matrix) - 1 and target < matrix[mid_point + 1][0]) or \
                            target > matrix[len(matrix) - 1][0] or len(matrix) == 1:
                first = 0
                while first <= last_column and not found:
                    column_mid_point = int((first + last_column) / 2)
                    if matrix[mid_point][column_mid_point] == target:
                        return True

                    if target > matrix[mid_point][column_mid_point]:
                        first = column_mid_point + 1
                    else:
                        last_column = column_mid_point - 1

            first = mid_point + 1
        else:
            if (mid_point - 1 >= 0) and target > matrix[mid_point - 1][0]:
                # print matrix[mid_point][0], matrix[mid_point - 1][0]
                first = 0
                while first <= last_column and not found:
                    column_mid_point = int((first + last_column) / 2)
                    if matrix[mid_point-1][column_mid_point] == target:
                        return True

                    if target > matrix[mid_point-1][column_mid_point]:
                        first = column_mid_point + 1
                    else:
                        last_column = column_mid_point - 1

            last_row = mid_point - 1
    return found

matrix = [[-8,-7,-5,-3,-3,-1,1],[2,2,2,3,3,5,7],[8,9,11,11,13,15,17],[18,18,18,20,20,20,21],[23,24,26,26,26,27,27],[28,29,29,30,32,32,34]]

target = -5
print(search_matrix(matrix, target))
