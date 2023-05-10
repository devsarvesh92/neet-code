from typing import Any


def longest_substr_wo_rep(input: str):
    """
    Given a string, find the length of the longest substring without repeating characters.
    For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.
    For "bbbbb" the longest substring is "b", with the length of 1.

    :param input: string
    :return: length of longest substring without repeating characters.
    """
    "abcabcbb"

    if len(input) == 0:
        return 0

    tracker: dict[str, Any] = {}
    start = max_length = 0

    for id, ch in enumerate(input):
        if ch in tracker and start <= tracker[ch]:
            start = tracker[ch] + 1
        else:
            max_length = max(max_length, id - start + 1)
        tracker[ch] = id
    return max_length


print(longest_substr_wo_rep("abcdabcbb"))
