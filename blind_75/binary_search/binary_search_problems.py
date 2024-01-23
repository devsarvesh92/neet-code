def search_element(nums: list[int], num: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if num < nums[mid]:
            r = mid - 1
        elif num > nums[mid]:
            l = mid + 1
        else:
            return mid
    return -1
