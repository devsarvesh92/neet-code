def productExceptSelf(nums: list[int]) -> list[int]:
    result = []
    current_prod = 1
    # compute pre fix prod
    for id, num in enumerate(nums):
        if id == 0:
            result.append(1)
            current_prod = num
            continue
        result.append(current_prod)
        current_prod = current_prod * num

    current_prod = 1
    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            current_prod = nums[i]
            continue
        result[i] = result[i] * current_prod
        current_prod = current_prod * nums[i]

    return result


print(productExceptSelf([-1, 1, 0, -3, 3]))
