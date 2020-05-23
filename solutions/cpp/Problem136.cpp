#pragma once
/*
136. Single Number

Given a non - empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity.Could you implement it without using extra memory ?
*/
#include <vector>


class Solution136 {
public:
	int singleNumber(std::vector<int>& nums) {
		int num = 0;
		for (auto & n : nums)
		{
			num ^= n;
		}
		return num;
	}
	void test() {

	}
}; 
