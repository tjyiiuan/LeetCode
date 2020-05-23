#pragma once
/*
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.

You may assume that the array is non-empty and the majority element always exist in the array.
*/
#include <map>
#include <iostream>
#include <vector>


class Solution169 {
public:
	int majorityElement(std::vector<int>& nums)	{
		std::map<int, int> count;
		for (auto &n : nums)
		{
			if (count.find(n) != count.end())
			{
				count[n] += 1;
			}
			else
			{
				count[n] = 1;
			}
		}

		int app = -1;
		int result = 0;
		for (std::map<int, int>::iterator it = count.begin(); it != count.end(); it++)
		{
			if (it->second > app)
			{
				app = it->second;
				result = it->first;
			}
		}
		return result;
	}
	void test()	{
		std::vector<int> test = { 2,2,1,1,1,2,2 };
		std::cout << majorityElement(test) << std::endl;
	}

};
