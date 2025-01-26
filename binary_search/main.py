from typing import List


# BINARY SEARCH
# Search for target in given list and return its index using O(log n)
def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

#print(search([1, 4, 6, 7, 8, 8, 9, 10], 6))

# SEARCH A 2D MATRIX
# You are given an m x n 2-D integer array matrix and an integer target.
# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.
# solution that runs in O(log(m * n)) time
#
# Ex:
# Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
# Output: true
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True
        elif current < target:
            row += 1
        else:
            col -= 1

    return False

#print(searchMatrix([[1,2,4,8],[10,11,12,13],[14,20,30,40]], 10))


#KOKO EATING BANANAS
# You are given an integer array piles where piles[i] is the number of bananas in the ith pile.
# You are also given an integer h, which represents the number of hours you have to eat all the bananas.
# You may decide your bananas-per-hour eating rate of k. Each hour, you may choose a pile of bananas and eats k bananas from that pile.
# If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.
# Return the minimum integer k such that you can eat all the bananas within h hours.
#
# Example 1:
# Input: piles = [1,4,3,2], h = 9
# Output: 2
# Explanation: With an eating rate of 2, you can eat the bananas in 6 hours. With an eating rate of 1,
#you would need 10 hours to eat all the bananas (which exceeds h=9), thus the minimum eating rate is 2.
def minEatingRate(piles: List[int], h: int) -> int:
    min_eating_rate = 1

    while min_eating_rate <= max(piles):
        temp_h = h
        for elem in piles:
            if temp_h < 0:
                break

            if elem <= min_eating_rate:
                temp_h -= 1
            else:
                if elem > min_eating_rate and temp_h > 0:
                    while elem > 0:
                        elem -= min_eating_rate
                        temp_h -= 1

        if temp_h >= 0:
            return min_eating_rate

        min_eating_rate += 1

    return min_eating_rate




#perform binary search over the possibilities of k (eating rate)
def getHoursForCurrentEatingRate(piles, current_eating_rate):
    hours = 0
    for pile in piles:
        # get nr of hours per pile (get ceiling)
        hours += (pile // current_eating_rate) + (1 if pile % current_eating_rate != 0 else 0)

    return hours # total hours for all piles with current rate
def minEatingRateBinarySearch(piles: List[int], h: int) -> int:
    right = max(piles)
    left = 1 # 1 is minimum bc KOKO cannot eat 0 bananas
    temp_result = right

    while left <= right:
        min_eating_rate = (left + right) // 2
        hours = getHoursForCurrentEatingRate(piles, min_eating_rate)

        if hours <= h:
            temp_result = min_eating_rate
            right = min_eating_rate - 1
        else:
            left = min_eating_rate + 1

    return temp_result


print(minEatingRateBinarySearch([3, 6, 7, 11], 8))