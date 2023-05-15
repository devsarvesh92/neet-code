def twoSum(nums: list[int], target: int) -> list[int]:

    for id, num in enumerate(nums):
        diff = target - num
        if pair := nums.index(diff):
            return [id, pair]


print(twoSum(nums=[2, 7, 11, 15], target=9))
