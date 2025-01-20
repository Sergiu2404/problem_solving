from typing import List


def removeDuplicates(nums: List[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
        if(nums[i] != nums[i - 1]):
            nums[j] = nums[i]
            j += 1

    return j



if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 10, 10]
    k = removeDuplicates(nums)
    print(k)
