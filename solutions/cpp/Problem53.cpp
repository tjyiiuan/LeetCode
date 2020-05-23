#pragma once
/*
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/
#include <iostream>
#include <vector>


class Solution53 {
public:
	int maxSubArray(std::vector<int>& nums)	{
		if (nums.empty())
		{
			return 0;
		}
		int max = nums[0];
		int size = nums.size();
		for (int i = 0; i < size; i++)
		{
			int nSum = nums[i];
			if (nSum > max)
			{
				max = nSum;
			}

			for (int j = i + 1; j < size; j++)
			{
				nSum += nums[j];
				if (nSum > max)
				{
					max = nSum;
				}
			}
		}
		return max;
	}
	void test()	{
		std::vector<int> nums;
		nums.push_back(-2);
		nums.push_back(1);
		nums.push_back(-3);
		nums.push_back(4);
		nums.push_back(-1);
		nums.push_back(2);
		nums.push_back(1);
		nums.push_back(-5);
		nums.push_back(4);
		std::cout << maxSubArray(nums) << std::endl;
	}
}; 
