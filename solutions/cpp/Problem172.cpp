#pragma once
/*
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.
*/
#include <iostream>


class Solution172 {
public:
	int trailingZeroes(int n) {
		int count = 0;
		for (long long factor = 5; factor <= n; factor *= 5)
		{
			count += n / factor;
		}
		return count;
	}
	void test()	{
		std::cout << trailingZeroes(5) << std::endl;
	}
}; 
