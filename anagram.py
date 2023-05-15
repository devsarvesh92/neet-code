def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    os = {}
    cs = {}
    for i in range(len(s)):

        # original input
        if s[i] in os:
            os[s[i]] = os[s[i]] + 1
        else:
            os[s[i]] = 1

        # compare input
        if t[i] in cs:
            cs[t[i]] = cs[t[i]] + 1
        else:
            cs[t[i]] = 1

    for k, v in os.items():
        if cs.get(k) != v:
            return False

    return True


print(isAnagram("anagram", "nagaram"))
