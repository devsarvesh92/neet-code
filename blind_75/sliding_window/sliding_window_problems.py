import string


def max_profit(prices: list[int]) -> int:
    profit = 0
    l, r = 0, 1
    while r < len(prices):
        bp = prices[l]
        sp = prices[r]
        profit = max(profit, sp - bp)
        if sp < bp:
            l = r
        r += 1
    return profit


def longest_substring_without_rep_chars(input: str):
    i, j = 0, 0
    window = set()
    long_len = 0
    while j < len(input):
        if input[j] not in window:
            window.add(input[j])
            long_len = max(len(window), long_len)
            j += 1
        else:
            i += 1
            j = i
            window = set()
    return long_len


def longest_rep_char_replacement(s: str, k: int) -> int:
    counter = dict.fromkeys(string.ascii_uppercase, 0)
    max_occurence = 0
    i, j = 0, 0
    max_len = 0
    # AABABBA

    while j < len(s):
        counter[s[j]] += 1
        max_occurence = max(counter[s[j]], max_occurence)
        window_len = j - i + 1
        if window_len - max_occurence <= k:
            max_len = max(max_len, window_len)
        else:
            counter[s[i]] -= 1
            i += 1
        j += 1
    return max_len
