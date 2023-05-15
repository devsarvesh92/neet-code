def contains_duplicate(input: list[int]):
    im_set = set()
    for num in input:
        if num in im_set:
            return True
        im_set.add(num)


if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))
