#pragma once
/*
27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.
*/
#include <iostream>
#include <vector>


class Solution27 {
public:
	int removeElement(std::vector<int>& nums, int val)	{
		for (std::vector<int>::iterator it = nums.begin(); it != nums.end();)
		{
			int thisVal = *it;
			if (thisVal == val)
			{
				it = nums.erase(it);
			}
			else
			{
				it++;
			}
		}
		return nums.size();
	}
	void test()	{
		std::vector<int> vecTest;
		int len = removeElement(vecTest, 1);
		for (int i = 0; i < len; i++)
		{
			std::cout << vecTest[i] << std::endl;
		}
	}
};

