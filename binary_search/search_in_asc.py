def bianry_search(*, input: list[int], target: int) -> int:
    l_ptr, r_ptr = 0, len(input) - 1
    while l_ptr <= r_ptr:
        mid = (l_ptr + r_ptr) // 2
        if target < input[mid]:
            r_ptr = mid - 1
        elif target > input[mid]:
            l_ptr = mid + 1
        else:
            return mid
    return -1
