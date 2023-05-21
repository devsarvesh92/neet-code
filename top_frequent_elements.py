from collections import defaultdict


def top_frequent_elements(nums: list[int], k: int):
    counter = defaultdict(int)
    frequent_el = []
    ls = [None for _ in range(len(nums))]
    for num in nums:
        if num in counter:
            counter[num] += 1
        else:
            counter[num] = 1

    for key, v in counter.items():
        ls[v] = key

    for i in range(len(nums) - 1, 0, -1):
        if len(frequent_el) == k:
            return frequent_el
        if ls[i]:
            frequent_el.append(ls[i])


print(top_frequent_elements([1, 1, 1, 2, 2, 3], k=2))
