import re


def valid_palindrome(*, input: str) -> bool:
    """
    Check if input is valid palindrome
    """
    # re.sub(pattern, replacement, string, count=0, flags=0)
    fmt_input: str = re.sub("[^a-zA-Z0-9]+", "", input)
    fmt_input = fmt_input.lower()

    i, j = 0, len(fmt_input) - 1

    while i < j:
        if fmt_input[i] != fmt_input[j]:
            return False
        i += 1
        j -= 1
    return True


def valid_plaindrome_opt(*, input) -> bool:
    def is_alpha_num(ip: str):
        if (ord("a") <= ord(ip) <= ord("z")) or (ord("0") <= ord(ip) <= ord("9")):
            return True
        return False

    i, j = 0, len(input) - 1
    while i < j:
        if not is_alpha_num(input[i]):
            i += 1
        if not is_alpha_num(input[j]):
            j -= 1

        if input[j] != input[j]:
            return False
        i, j = i + 1, j - 1
    return True


# print(valid_palindrome(input="ab_a"))
print(valid_plaindrome_opt(input="ab_a"))
