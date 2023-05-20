from collections import defaultdict


def group_anagrams(input: list[str]) -> list[list[str]]:
    """
    Complexity - > O[n * m log(m)]
    """
    grouped_anagrams: dict[int, list[str]] = {}

    for ip in input:
        sorted_str = "".join(sorted(ip))
        if sorted_str in grouped_anagrams:
            grouped_anagrams[sorted_str].append(ip)
        else:
            grouped_anagrams[sorted_str] = [ip]

    return [v for k, v in grouped_anagrams.items()]


def group_anagrams_opt(input: list[str]) -> list[list[str]]:

    grouped_anagrams = defaultdict(list)
    for ip in input:
        count = [0] * 26
        for c in ip:
            count[ord(c) - ord("a")] += 1

        grouped_anagrams[tuple(count)].append(ip)
    return grouped_anagrams.values()


print(group_anagrams_opt(["eat", "tea", "tan", "ate", "nat", "bat"]))
