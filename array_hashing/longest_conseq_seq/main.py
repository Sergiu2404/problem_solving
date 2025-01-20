def longest_consecutive_seq(nums):
    numsSet = set(nums)
    print(set(nums))
    length = 0
    max_len = 1

    for elem in numsSet:
        if elem - 1 not in numsSet: #pass over the elements already parsed for efficiency
            length = 0
            while elem + length in numsSet:
                length+=1

        max_len = max(length, max_len)

    return max_len

print(longest_consecutive_seq([9,1,4,7,3,-1,0,5,8,-1,6]))