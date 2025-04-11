#include "permutation_find_first_asc_bin_search.h";


int main() {
	vector<int> nums = { 5, 6, 1, 2, 3, 4 };
	int pos = find_pos_first_asc_elem_permutation(nums);

	cout << pos;
	return 0;
}