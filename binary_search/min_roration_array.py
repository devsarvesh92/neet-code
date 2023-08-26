def get_min_after_rotating_array(input: list[int]) -> int:
    res = input[0]
    l, r = 0, len(input) - 1
    while l <= r:
        if input[l] < input[r]:
            return min(res, input[l])
        mid = (l + r) // 2
        res = min(input[mid], res)

        if input[mid] >= input[l]:
            l = mid + 1
        else:
            r = mid - 1
    return res
