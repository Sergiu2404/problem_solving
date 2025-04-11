// {5, 6, 1, 2, 3, 4} for this returns position of elem 1 (position 2) because first elem in ascending order after permuted to the right
#include <iostream>
#include <vector>
#include "permutation_find_first_asc_bin_search.h";
using namespace std;

int find_pos_first_asc_elem_permutation(vector<int> nums) {
	int l = 0, r = nums.size() - 1;

	while (l < r) {
		int mid = (l + r) / 2;

		if (nums[r] < nums[mid]) // then the element is in the right side
			l = mid + 1;
		else // else search in the left
			r = mid;
	}

	return l;
}