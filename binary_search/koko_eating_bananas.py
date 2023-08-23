import math


def get_min_rate_for_koko_eating_banana(piles: list[int], h: int) -> int:
    max_pile = max(piles)
    ips = list(range(1, max_pile + 1))

    l_ptr, rptr = (0, len(ips) - 1)

    while l_ptr <= rptr:
        middle = (l_ptr + rptr) // 2
        # check if middle is sufficient rate
        total_time_taken = math.ceil(sum([p / ips[middle] for p in piles]))
        if total_time_taken <= h:
            # found a match
            # check for better possiblity
            rptr = middle - 1
        else:
            l_ptr = middle + 1
    return ips[middle]
