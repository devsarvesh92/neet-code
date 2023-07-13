def daily_tempratures(*, input: list[int]) -> list[int]:
    """Daily tempratures, monotonic decreasing order"""
    res = [0] * len(input)
    stack = []  # param [val,pos]

    for id, val in enumerate(input):
        while stack and val > stack[-1][0]:
            av, ap = stack.pop()
            res[ap] = id - ap
        stack.append([val, id])
    return res
