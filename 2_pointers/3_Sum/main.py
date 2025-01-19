from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()  # sort arr to use 2_pointer approach
    triplets = []

    for i in range(len(nums) - 2):
        # skip duplicate elements for i to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1

                # skip duplicate elems for left
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # skip duplicate elems for right
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif current_sum < 0:
                left += 1  # go left to incr sum
            else:
                right -= 1  # go right to decrease sum

    return triplets

print(threeSum([1, 1, 0, -1, 2, -1, 4, 2, 3]))