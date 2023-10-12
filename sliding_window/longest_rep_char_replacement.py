def get_longest_rep_char_replacement(k: int, input: str) -> int:
    counter = {chr(i): 0 for i in range(65, 91)}
    i, j = 0, 0
    res = 0

    while j < len(input):
        end_alpha = input[j]
        counter[end_alpha] += 1
        window_size = (j - i) + 1
        max_rep_char = max(counter.values())

        if (window_size - max_rep_char) > k:
            start_alpha = input[i]
            counter[start_alpha] -= 1
            i += 1
            j += 1
            continue
        else:
            res = max(res, window_size)
            j += 1

    return res


assert 4 == get_longest_rep_char_replacement(k=2, input="ABAB")
assert 4 == get_longest_rep_char_replacement(k=1, input="AABABBA")
