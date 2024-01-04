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
