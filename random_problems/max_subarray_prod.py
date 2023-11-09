def get_max_product(nums: list[int]) -> int:
    res = max(nums)
    curr_max, curr_min = 1, 1

    for n in nums:
        if n == 0:
            curr_max, curr_min = 1, 1
        tmp = curr_max * n
        curr_max = max(n * curr_max, n * curr_min, n)
        curr_min = max(tmp, n * curr_min, n)
        res = max(curr_max, curr_min, n)
    return res


if __name__ == "__main__":
    assert 6 == get_max_product(nums=[1, 2, 3])
