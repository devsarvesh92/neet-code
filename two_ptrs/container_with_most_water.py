def container_with_most_water(*, input: list[int]) -> int:
    """Find a container with max height

    Args:
        input (list[int]): _description_

    Returns:
        int: _description_
    """

    i, j = 0, len(input) - 1
    max_area = 0

    while i < j:
        height = min(input[i], input[j])
        width = abs(j - i)
        area = height * width
        max_area = max(area, max_area)
        if input[i] > input[j]:
            j -= 1
        else:
            i += 1
    return max_area


print(container_with_most_water(input=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
