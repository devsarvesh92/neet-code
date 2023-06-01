
def longest_cons_sequence(nums:list[int])-> int:
    st = set(nums)
    longest = 0
    for n in nums:
        if (n-1) not in st:
            length = 0
            while n+length in nums:
                length+=1
            longest = max(length,longest)
    return longest

print(longest_cons_sequence([100,4,200,1,3,2]))
            