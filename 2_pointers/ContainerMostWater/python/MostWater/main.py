from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        st = 0
        end = len(height) - 1
        maxArea = 0

        while st <= end:
            if min(height[st], height[end]) * (end - st) >= maxArea:
                maxArea = min(height[st], height[end]) * (end - st)
            if height[st] < height[end]:
                st += 1
            else:
                end -= 1

        return maxArea



if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([4,3,2,1,4]))