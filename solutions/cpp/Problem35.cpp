#pragma once
/*
35. Search Insert Position

Given a sorted array and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
*/
#include <iostream>
#include <vector>


class Solution {
public:
	int searchInsert(std::vector<int>& nums, int target) {
		if (nums.empty())
		{
			return 0;
		}
		int size = nums.size();
		if (nums[size - 1] < target)
		{
			return size;
		}
		else if (nums[0] >= target)
		{
			return 0;
		}
		for (int i = 0; i < nums.size(); i++)
		{
			if (nums[i] >= target)
			{
				return i;
			}
		}
		return 0;
	}
	void test()	{
		std::vector<int> nums;
		nums.push_back(1);
		nums.push_back(3);
		nums.push_back(5);
		nums.push_back(6);
		std::cout << searchInsert(nums, 5) << std::endl;
		std::cout << searchInsert(nums, 2) << std::endl;
		std::cout << searchInsert(nums, 7) << std::endl;
		std::cout << searchInsert(nums, 0) << std::endl;
	}
}; 
