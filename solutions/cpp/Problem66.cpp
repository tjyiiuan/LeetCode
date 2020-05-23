#pragma once
/*
66. Plus One

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
*/
#include <iostream>
#include <vector>


class Solution66 {
public:
	std::vector<int> plusOne(std::vector<int>& digits) {
		std::vector<int> result;
		int of = 0;
		int num = 0;
		for (std::vector<int>::iterator it = digits.end(); it != digits.begin(); it--)
		{
			num = *(it - 1) + of;
			if (it == digits.end())
			{
				num += 1;
			}
			of = 0;
			if (num >= 10)
			{
				num = num % 10;
				of = 1;
			}
			result.insert(result.begin(), num);
		}
		if (of > 0)
		{
			result.insert(result.begin(), of);
		}
		return result;
	}
	void test()	{
		std::vector<int> nums = { 9,9,9 };
		for (auto &i : plusOne(nums))
		{
			std::cout << i << std::endl;
		}
	}
};
