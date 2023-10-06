def get_max_profit(*, prices: list[int]) -> int:
    l_ptr, r_ptr = 0, 1
    current_profit = 0
    while r_ptr < len(prices):
        val1 = prices[l_ptr]
        val2 = prices[r_ptr]
        current_profit = max(current_profit, val2 - val1)
        if val1 > val2:
            l_ptr = r_ptr
        r_ptr += 1
    return current_profit
