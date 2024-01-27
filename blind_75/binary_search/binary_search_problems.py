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


def search_in_rotated_array(*, nums: list[int], target: int) -> int:
    # [5,1]

    # If middle in 1st sorted half and start of array is less than target search in first half else 2nd half
    i, j = 0, len(nums) - 1
    while i <= j:
        mid_idx = (i + j) // 2
        middle = nums[mid_idx]
        start = nums[i]
        end = nums[j]
        if target > middle:
            if middle >= start:
                i = mid_idx + 1
            else:
                if end >= target:
                    i = mid_idx + 1
                else:
                    j = mid_idx - 1
        elif target < middle:
            if middle >= start:
                if start <= target:
                    j = mid_idx - 1
                else:
                    i = mid_idx + 1
            else:
                j = mid_idx - 1
        else:
            return mid_idx

    return -1
