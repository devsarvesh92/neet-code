def is_valid(*, input: str) -> bool:
    """Check if parentheses is valid"""

    stack = []
    matching_pairs = {")": "(", "}": "{", "]": "["}

    for ch in input:
        if ch in matching_pairs:
            if matching_pairs[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return True if not stack else False


print(is_valid(input="(]"))
