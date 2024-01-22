def valid_parenttheses(s: str) -> bool:
    valid_pairs: dict[str, str] = {"(": ")", "{": "}", "[": "]"}
    stack: list[str] = []

    for c in s:
        if c in valid_pairs:
            stack.append(c)
        else:
            recent_el = stack[-1]
            if valid_pairs[recent_el] != c:
                return False
    return True
