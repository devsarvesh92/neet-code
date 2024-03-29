import re


def is_palindrome(s: str) -> bool:
    s = re.sub("[^a-zA-Z0-9]+", "", s)
    s = s.lower()

    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True


def three_sum(nums: list[int]) -> list[list[int]]:
    target_sum = 0
    nums.sort()
    result = []
    for id, num in enumerate(nums):
        i, j = id + 1, len(nums) - 1

        while i < j:
            current_sum = num + nums[i] + nums[j]
            if target_sum == current_sum:
                if [num, nums[i], nums[j]] not in result:
                    result.append([num, nums[i], nums[j]])
                i += 1
                j -= 1
            elif current_sum > target_sum:
                j -= 1
            elif current_sum < target_sum:
                i += 1
    return result


def container_with_most_water(height:list[int])->int:
    i,j = 0,len(height)-1
    max_area=0
    while i < j:
        width =abs(i-j)
        ht = min(height[i],height[j])
        max_area = max(width*ht,max_area)
        if height[i] < height[j]:
            i+=1
        else:
            j-=1
    return max_area

