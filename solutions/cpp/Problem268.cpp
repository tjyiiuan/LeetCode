#pragma once
/*
268. Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
*/
#include <vector>


class Solution {
public:
	int missingNumber(std::vector<int>& nums) {
		int res = (nums.size() + 1) * nums.size() / 2;
		for (auto &i : nums) {
			res -= i;
		}
		return res;
	}
};
