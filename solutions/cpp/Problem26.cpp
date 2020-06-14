#pragma once
/*
26. Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
*/
#include <iostream>
#include <vector>


class Solution {
public:
	int removeDuplicates(std::vector<int>& nums) {
		if (nums.size() == 1)
		{
			return 1;
		}

		int last;
		for (std::vector<int>::iterator it = nums.begin(); it != nums.end();)
		{
			if (it == nums.begin())
			{
				last = *it;
				it++;
				continue;
			}
			int thisVal = *it;
			if (thisVal == last)
			{
				it = nums.erase(it);
			}
			else
			{
				it++;
			}
			last = thisVal;
		}
		return nums.size();
	}
	void test()	{
		std::vector<int> vecTest;
		vecTest.push_back(1);
		vecTest.push_back(1);
		vecTest.push_back(2);
		int len = removeDuplicates(vecTest);
		for (int i = 0; i < len; i++)
		{

			std::cout << vecTest[i] << std::endl;
		}
	}
};
