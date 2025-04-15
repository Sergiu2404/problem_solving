#include <iostream>
#include <vector>
#include "has_pair_sum.h";
using namespace std;

bool hasPairWithSum(const vector<int>& nums, int target) {
    int left = 0;
    int right = nums.size() - 1;

    while (left < right) {
        int sum = nums[left] + nums[right];

        if (sum == target) return true;
        else if (sum < target) left++;
        else right--;
    }

    return false;
}
