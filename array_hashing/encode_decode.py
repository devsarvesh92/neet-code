import re


def encode(input: list[str]) -> str:
    """
    Given input as a list of str return op str
    """
    encoded_str: str = ""
    for ip in input:
        encoded_str += f"{len(ip)}#{ip}"
    return encoded_str


def decode_with_regex(input: str) -> list[str]:
    return re.split("\d#", input)[1:]


def decode_wthout_regex(input: str) -> list[str]:

    "4#lint4#code4#love3#you"
    i = 0
    ls = []
    while i < len(input):
        j = i
        while input[j] != "#":
            j += 1
        num = int(input[i:j])
        word = input[j + 1 : j + num + 1]
        ls.append(word)
        i = j + num + 1
    return ls


print(decode_wthout_regex(encode(input=["lint", "code", "love", "you"])))
