#pragma once
/*
189. Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.
*/
#include <iostream>
#include <vector>


class Solution {
public:
	void rotate(std::vector<int>& nums, int k) {
		if (k <= 0)
		{
			return;
		}

		if (k > nums.size())
		{
			k = k % nums.size();
		}

		for (int i = 0; i < k; i++)
		{
			std::vector<int>::iterator it = nums.end() - 1;
			nums.insert(nums.begin(), *it);
			nums.pop_back();
		}
	}
	void test()	{
		std::vector<int> test = { 1,2,3,4,5,6,7 };
		rotate(test, 3);
		for (auto &i : test)
		{
			std::cout << i << std::endl;
		}
	}
}; 
