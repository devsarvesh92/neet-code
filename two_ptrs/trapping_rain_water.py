def trap(heights: list[int]) -> int:
    max_l, max_r = 0, 0
    l, r = 0, len(heights) - 1
    water_level = 0
    while l < r:
        if max_l < max_r:
            l += 1
            max_l = max(heights[l], max_l)
            water_level += max_l - heights[l]
        else:
            r -= 1
            max_r = max(heights[r], max_r)
            water_level += max_r - heights[r]
    return water_level


print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
