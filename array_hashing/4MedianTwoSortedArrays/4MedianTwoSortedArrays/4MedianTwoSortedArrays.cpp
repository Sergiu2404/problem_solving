#include <iostream>
#include <vector>
using namespace std;

vector<int> mergeArrays(vector<int>& nums1, vector<int>& nums2) {
    int i = 0, j = 0, k = 0;
    vector<int> mergedArray;

    while (i < nums1.size() && j < nums2.size())
    {
        if (nums1[i] <= nums2[j])
        {
            mergedArray.push_back(nums1[i]);
            i++;
        }
        else
        {
            mergedArray.push_back(nums2[j]);
            j++;
        }
    }

    while (i < nums1.size())
    {
        mergedArray.push_back(nums1[i]);
        i++;
    }
    while (j < nums2.size())
    {
        mergedArray.push_back(nums2[j]);
        j++;
    }

    return mergedArray;
}
double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    vector<int> result = mergeArrays(nums1, nums2);

    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
    cout << endl;

    if (result.size() % 2 == 1)
    {
        return (double)result[(result.size() - 1) / 2];
    }
    else
    {
        return (double)(result[result.size() / 2 - 1] + result[result.size() / 2]) / 2;
    }
}

int main()
{
    /*vector<int>nums1{ 1, 2, 7, 8, 11, 23 };
    vector<int>nums2{ 1, 3, 4, 5, 6, 25, 29, 31 };*/
    vector<int>nums1{ 1, 2};
    vector<int>nums2{3, 4};
    
    cout << findMedianSortedArrays(nums1, nums2);
}