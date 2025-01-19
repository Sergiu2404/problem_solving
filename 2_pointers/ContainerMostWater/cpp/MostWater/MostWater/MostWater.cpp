// MostWater.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0, end = height.size() - 1;
        int maxArea = 0;

        while (start <= end) {
            int minHeight = height[start] < height[end] ? height[start] : height[end];
            if (minHeight * (end - start) > maxArea)
            {
                maxArea = minHeight * (end - start);
            }
            if (height[start] < height[end])
            {
                start++;
            }
            else {
                end--;
            }
        }

        return maxArea;

    }
};


int main()
{
    Solution solution = Solution();
    vector<int> height = { 1,8,6,2,5,4,8,3,7 };
    cout << solution.maxArea(height);
}
