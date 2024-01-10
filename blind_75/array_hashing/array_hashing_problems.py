from collections import defaultdict


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


def bubble_sort(*, nums: list[int]) -> list[int]:
    for i in range(0, len(nums) - 1):
        swapped = False
        for j in range(0, len(nums) - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            return nums


def get_prime_numbers(*, start: int, end: int) -> list[int]:
    prime_nums = []
    for num in range(1, end):
        flag = True
        for child in range(2, num):
            if num % child == 0:
                flag = False
                break
        if flag:
            prime_nums.append(num)
    return prime_nums


def validate_sudoku_board(*, board: list[list[str]]) -> bool:
    col = defaultdict(set)
    row = defaultdict(set)
    square = defaultdict(set)

    for r in range(9):
        for c in range(9):
            value = board[r][c]

            if value == ".":
                continue

            if value in row[r] or value in col[c] or value in square[(r // 3, c // 3)]:
                return False
            else:
                col[c].add(value)
                row[r].add(value)
                square[(r // 3, c // 3)].add(value)
    return True


def get_longest_consecutive_sequence(nums: list[int]) -> list[int]:
    unique_nums = set(nums)
    longest_seq = 0
    for num in nums:
        if (num - 1) not in unique_nums:
            nxt_el = num + 1
            length = 1
            while nxt_el in unique_nums:
                length += 1
                nxt_el += 1
            longest_seq = max(length, longest_seq)
    return longest_seq
