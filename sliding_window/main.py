from typing import List


def brute_force(interval_size, array):
    i = 0
    curr_max = float('-inf')

    if len(array) <= interval_size:
        return sum(array)

    while i + interval_size < len(array):
        sum_interval = 0
        for j in range(interval_size):
            sum_interval += array[i + j]

        curr_max = curr_max if curr_max > sum_interval else sum_interval
        i += 1

    return curr_max


# print(brute_force(4, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 10]))


def sliding_window(window_size, array):
    curr_sum = 0
    curr_max = 0

    for j in range(window_size):
        curr_sum += array[j]

    start = 0
    end = window_size
    while end < len(array):
        curr_sum = curr_sum - array[start] + array[end]
        curr_max = max(curr_sum, curr_max)
        start += 1
        end += 1

    return curr_max

#print(sliding_window(4, [1, 2, 3, 4, 5, 6, 7, 1, 2, 3, 10]))




#BEST TIME TO BUY AND SELL STOCK
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.
# Ex 1:
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
def maxProfit(prices: List[int]) -> int:
    if sorted(prices, reverse=True) == prices:
        return 0

    start = 0
    end = 1

    profit = 0
    while end < len(prices):
        if prices[start] < prices[end]:
            profit = max(prices[end] - prices[start], profit)
        else:
            start = end

        end += 1

    return profit

print(maxProfit([10,1,5,6,7,1]))
