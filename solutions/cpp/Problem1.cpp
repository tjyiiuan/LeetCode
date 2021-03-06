#pragma once
/*
1. Two Sum

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
*/
#include <vector>
#include <iostream>


class Solution {
public:
	std::vector<int> twoSum(std::vector<int> &vec, int target) {
		std::vector<int> result;
		int size = vec.size();
		for (int i = 0; i < size - 1; i++)
		{
			for (int j = i + 1; j < size; j++)
			{
				if (vec[i] + vec[j] == target)
				{
					result.push_back(i);
					result.push_back(j);
					break;
				}
			}
		}
		return result;
	}
	void test() {
		std::vector<int> vecSum;
		vecSum.push_back(2);
		vecSum.push_back(7);
		vecSum.push_back(4);
		vecSum.push_back(6);
		std::vector<int> solution = twoSum(vecSum, 9);
		for (auto &k : solution)
		{
			std::cout << k << std::endl;
		}
	}
};

