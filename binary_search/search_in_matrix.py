def search_matrix(*, input: list[list[int]], target: int) -> bool:
    l_row, r_row = (0, len(input) - 1)

    while l_row <= r_row:
        mid_row = (l_row + r_row) // 2
        if target <= input[mid_row][-1] and target >= input[mid_row][0]:
            target_row = input[mid_row]
            l_ptr, r_ptr = (0, len(target_row) - 1)
            while l_ptr <= r_ptr:
                mid = (l_ptr + r_ptr) // 2
                if target > target_row[mid]:
                    l_ptr = mid + 1
                elif target < target_row[mid]:
                    r_ptr = mid - 1
                else:
                    return True
        elif target > input[mid_row][-1]:
            l_row = mid_row + 1
        elif target < input[mid_row][0]:
            r_row = mid_row - 1
    return False
