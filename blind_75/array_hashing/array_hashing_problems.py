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
    el_counter: dict[int, int] = {}

    for el in nums:
        if el in el_counter:
            el_counter[el] += 1
        else:
            el_counter[el] = 1

    sorted_dict = {
        k: v
        for k, v in sorted(el_counter.items(), key=lambda item: item[1], reverse=True)
    }

    return list(sorted_dict.keys())[:k]


def array_product_except_self(*, nums: list[int]) -> list[int]:
    result = []
    current_product = 1
    for id, val in enumerate(nums):
        if id == 0:
            # No element before
            current_product = val
            result.append(1)
            continue
        result.append(current_product)
        current_product *= val

    current_product = 1

    for id in range((len(nums) - 1), -1, -1):
        if id == len(nums) - 1:
            result[id] = result[id] * 1
            current_product = nums[id]
            continue
        result[id] = result[id] * current_product
        current_product *= nums[id]

    return result
