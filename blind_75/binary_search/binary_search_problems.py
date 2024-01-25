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


def find_min(nums: list[int]) -> int:
    l, r = 0, len(nums) - 1
    min_num = nums[0]
    while l <= r:
        mid = (l + r) // 2
        min_num = min(min_num, nums[mid], nums[l], nums[r])
        middle = nums[mid]
        left = nums[l]
        if middle >= left:
            l = mid + 1
        else:
            r = mid - 1
    return min_num
