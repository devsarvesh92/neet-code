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
        if rem in kv:
            return [idx, kv[rem]]
