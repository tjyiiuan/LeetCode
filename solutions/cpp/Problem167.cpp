#pragma once
/*
167. Two Sum II - Input array is sorted

Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
*/
#include <vector>


class Solution {
public:
	std::vector<int> twoSum(std::vector<int>& numbers, int target) {
		std::vector<int> result;
		int n = numbers.size();
		for (int i = 0; i < n - 1; i++)
		{
			for (int j = i + 1; j < n; j++)
			{
				int cur = numbers[i] + numbers[j];
				if (cur == target)
				{
					result.push_back(i + 1);
					result.push_back(j + 1);
					return result;
				}
				else if (cur > target)
				{
					break;
				}
			}
		}
		return result;
	}
	void test() {

	}
};
