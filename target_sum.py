def twoSum(nums: list[int], target: int) -> list[int]:
    try:
        for id, num in enumerate(nums):
            diff = target - num
            if pair := nums.index(diff):
                return [id, pair]
    except ValueError:
        print("Ignore")


print(twoSum(nums=[3, 3], target=6))
