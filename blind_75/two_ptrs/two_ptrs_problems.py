import re


def is_palindrome(s: str) -> bool:
    s = re.sub("[^a-zA-Z0-9]+", "", s)
    s = s.lower()

    start, end = 0, len(s) - 1

    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1

    return True
