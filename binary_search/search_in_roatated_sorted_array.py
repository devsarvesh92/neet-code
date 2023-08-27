def search(*, input: list[int], target: int) -> int:
    l_ptr, r_ptr = 0, len(input) - 1
    while l_ptr <= r_ptr:
        mid = (l_ptr + r_ptr) // 2
        mid_dig = input[mid]
        lft_dig = input[l_ptr]
        rgt_dig = input[r_ptr]
        if mid_dig == target:
            return mid
        if mid_dig >= lft_dig:
            # middle is in lft sorted portion
            if target <= mid_dig and target >= lft_dig:
                r_ptr = mid - 1
            else:
                l_ptr = mid + 1
        else:
            # middle is in right sorted portion
            if target >= mid_dig and target <= rgt_dig:
                l_ptr = mid + 1
            else:
                r_ptr = mid - 1

    return -1
