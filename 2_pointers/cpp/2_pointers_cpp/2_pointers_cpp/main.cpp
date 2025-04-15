#include "has_pair_sum.h";
#include <iostream>
#include <vector>
#include <algorithm>
#include "rem_duplicates.h";
#include "swap_string.h";
using namespace std;


//int main() {
//    vector<int> nums = { 1, 2, 3, 4, 6 };
//    int target = 10;
//
//    if (hasPairWithSum(nums, target))
//        cout << "Pair found!" << endl;
//    else
//        cout << "No pair found." << endl;
//
//    return 0;
//}

int main(){
    vector<int> nums = { 1, 1, 2, 2, 3, 4, 4, 5 };
    int newLength = removeDuplicates(nums);
    cout << "After removing duplicates: ";
    for (int i = 0; i < newLength; i++) {
        cout << nums[i] << " ";
    }
    cout << endl;

    vector<char> s = { 'h', 'e', 'l', 'l', 'o' };
    reverseString(s);
    cout << "Reversed string: ";
    for (char c : s) {
        cout << c;
    }
    cout << endl;

    return 0;
}
