# sliding window
# [1,2,3,4,5,6]
# initial sum: 6
# next step : 6 -1 + 4 -> 9
# next step : 9-2+5 -> 12
# next step : 12-3+6 -> 15


def get_sum_of_sub_array_of_len(*, window_size: int, input: list[int]):
    initial_sum: int = sum(input[:window_size])
    computed_sums = []
    computed_sums.append(initial_sum)

    for i in range(1, len(input) - window_size + 1):
        initial_sum = initial_sum - input[i - 1] + input[i + window_size - 1]
        computed_sums.append(initial_sum)

    return computed_sums


print(get_sum_of_sub_array_of_len(window_size=3, input=[1, 2, 3, 4, 5, 6]))
