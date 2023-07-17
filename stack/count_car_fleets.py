def count_car_fleets(*, target, position, speed) -> int:
    # combine target and position
    # sort
    # check for colision
    # esentially only fleets would stay in stack

    target_position = list(zip(position, speed))
    stack = []
    sorted_arr = sorted(target_position)[::-1]
    for el in sorted_arr:
        curr_position = el[0]
        curr_speed = el[1]

        curr_time = (target - curr_position) / curr_speed
        stack.append(curr_time)
        if len(stack) >= 2 and stack[-2] >= stack[-1]:
            stack.pop()

    return len(stack)
