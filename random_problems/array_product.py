def get_array_product_except_number(nums: list[int]) -> list[int]:
    # [1, 2, 3, 4]
    result = [None] * len(nums)
    product = 1

    # prefix product
    for idx, num in enumerate(nums):
        result[idx] = product
        product *= num

    # postfix product
    product = 1
    current_idx_offset: int = len(nums) - 1
    for idx, num in enumerate(nums[::-1]):
        result[current_idx_offset - idx] *= product
        product *= num

    return result


if __name__ == "__main__":
    assert [24, 12, 8, 6] == get_array_product_except_number(nums=[1, 2, 3, 4])
