def check_duplicates(*, nums: list[int]) -> bool:
    if len(set(nums)) != len(nums):
        return True
    return False


def check_anagram(*, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def two_sum(*, nums: list[int], target: int) -> list[int]:
    kv = {val: id for id, val in enumerate(nums)}

    for idx, val in enumerate(nums):
        rem = target - val
        if (rem in kv) and (idx != kv[rem]):
            return [idx, kv[rem]]


def group_anagrams(*, input: list[str]) -> list[list[str]]:
    anagram_group: dict[str, list[str]] = {}

    for ip in input:
        sorted_ip: str = "".join(sorted(ip))
        if sorted_ip in anagram_group:
            anagram_group[sorted_ip].append(ip)
        else:
            anagram_group[sorted_ip] = [ip]

    return list(anagram_group.values())


def top_k_frequent_elements(*, nums: list[int], k: int) -> list[int]:
    elments_pos = [[]] * (len(nums) + 1)
    el_counter: dict[int, int] = {}
    for el in nums:
        if el in el_counter:
            el_counter[el] += 1
        else:
            el_counter[el] = 1

    for i in range(1, (len(nums) + 1)):
        elments_pos[i] = [k for k, v in el_counter.items() if v == i]

    flattend_list = [x for el in elments_pos for x in el]
    return flattend_list[-k:]
