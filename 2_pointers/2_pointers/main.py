#NEETCODE

# EVEN PALINDROME
from typing import List


def is_palindrome(string):
    newString = ""
    ind = 0

    for char in string:
        if char.isalpha() or char.isnumeric():
           newString = newString + char

    start = 0
    end = len(newString) - 1

    while start <= end:
        if newString[start].lower() != newString[end].lower():
            return False

        start+=1
        end-=1

    return True

# print(is_palindrome("0P"))
# print(is_palindrome("abba"))
# print(is_palindrome("Was it a car or a cat I saw?"))

# Two Integer Sum II
# Given an array of integers numbers that is sorted in non-decreasing order.
# Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number
# target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same
# element twice.
def twoSum(numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1

    # they are already sorted so we can use 2 indices start and end, if they add up to a nr less than target,
    # it means we need a greater number (being sorted we increase start), if > target we need to decrease end (smaller nr)
    while start <= end:
        if numbers[start] + numbers[end] > target:
            end-=1
        elif numbers[start] + numbers[end] > target:
            start+=1
        else:
            return [start, end]

#print(twoSum([1, 2, 3, 4], 3))

# 3_SUM
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
def threeSum(nums: List[int]) -> List[List[int]]:
    start = 0
    end = len(nums) - 1

    nums.sort()
    solution = []

    while start <= end - 2:
        mid = start + 1
        end = len(nums) - 1
        while mid < end: # 2 pointers
            if nums[start] + nums[end] + nums[mid] == 0:
                partial = [nums[start], nums[mid], nums[end]]
                if partial not in solution:
                    solution.append(partial)
                mid += 1
                end -= 1
            elif nums[start] + nums[end] + nums[mid] < 0:
                mid += 1
            else:
                end -= 1

        start += 1

    return solution

#print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
# print(threeSum([0, 0, 0, 0]))
# print(threeSum([-2,0,1,1,2]))


# CONTAINER WITH MOST WATER
# You are given an integer array heights where heights[i] represents the height of the i-th bar
# You may choose any two bars to form a container. Return the maximum amount of water a container can store.
def maxArea(heights: List[int]) -> int:
    # maxAr = float('-inf')
    #
    # for i in range(len(heights)):
    #     for j in range(i + 1, len(heights)):
    #         if min(heights[i], heights[j]) * (j - i) > maxAr:
    #             maxAr = min(heights[i], heights[j]) * (j - i)
    # return maxAr
    start = 0
    end = len(heights) - 1
    minim = float('+inf')
    maxAr = float('-inf')

    while start <= end:
        maxAr = max(maxAr, min(heights[start], heights[end]) * (end - start))
        if heights[start] > heights[end]:
            end -= 1
        else:
            start += 1

    return maxAr


# print(maxArea([2, 2, 2]))
# print(maxArea([1,7,2,5,4,7,3,6]))




# TRAPPING RAIN WATER
# You are given an array non-negative integers height which represent an elevation map. Each value height[i] represents the height of a bar, which has a width of 1.
# Return the maximum area of water that can be trapped between the bars.
# Example:
#Input: height = [0,2,0,3,1,0,1,3,2,1]
#Output: 9
def trap(height: List[int]) -> int:
    trappedWater = 0

    for mid in range(len(height)):
        leftMax = height[mid]
        rightMax = height[mid]

        for j in range(mid): # search max at the left of mid
            leftMax = max(leftMax, height[j])
        for j in range(mid + 1, len(height)): # search max at the right of mid
            rightMax = max(rightMax, height[j])

        trappedWater += min(leftMax, rightMax) - height[mid]

    return trappedWater


def trap_efficient(height: List[int]) -> int:
    prefixMax = [0] * len(height)
    suffixMax = [0] * len(height)
    trappedWater = 0

    prefixMax[0] = height[0]
    for i in range(1, len(height)): # max prefix
        prefixMax[i] = max(prefixMax[i - 1], height[i])

    suffixMax[len(height) - 1] = height[len(height) - 1]
    for i in range(len(height) - 2, -1, -1): # max suffix
        suffixMax[i] = max(suffixMax[i + 1], height[i])

    for i in range(len(height)): # for every index calculate using max at its left and max at its right
        trappedWater += min(prefixMax[i], suffixMax[i]) - height[i]

    return trappedWater

print(trap_efficient([0,2,0,3,1,0,1,3,2,1]))