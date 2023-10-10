def find_substr_wo_rep_chars(input: str):
    i, j = 0, 1
    max_length = 1
    curr_substr = f"{input[0]}"

    while j < len(input):
        if input[i] != input[j] and input[j] not in curr_substr:
            curr_substr = f"{curr_substr}{input[j]}"
            max_length = max(max_length, len(curr_substr))
        else:
            i = j
            curr_substr = f"{input[i]}"
        j += 1

    return max_length


assert 3 == find_substr_wo_rep_chars(input="abcabcbb")
assert 1 == find_substr_wo_rep_chars(input="bbbbb")
assert 3 == find_substr_wo_rep_chars(input="pwwkew")
