def target_indices(input: list[int], target_sum: int) -> list[list[int]]:
    input.sort()
    result = []

    for idx in range(len(input) - 3):
        if input[idx] == input[idx - 1]:
            continue

        i, j = (idx + 1, len(input) - 1)
        while i < j:
            curr_sum = input[idx] + input[i] + input[j]
            if curr_sum == target_sum:
                result.append([input[idx], input[i], input[j]])
                i += 1
                j -= 1
            elif curr_sum > target_sum:
                j -= 1
            elif curr_sum < target_sum:
                i += 1
    return result


print(target_indices([-1, 0, 1, 2, -1, -4], 0))
