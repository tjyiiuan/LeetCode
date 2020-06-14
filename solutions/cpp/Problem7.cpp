#pragma once
/*
7. Reverse Integer

Given a 32-bit signed integer, reverse digits of an integer.
*/
#include <iostream>
#include <vector>
#include <string>


class Solution {
public:
	int reverse(int x)	{
		long long result = 0;
		while (x != 0)
		{
			result *= 10;
			result += x % 10;
			x /= 10;
		}
		if (result > INT_MAX || result < INT_MIN)
		{
			return 0;
		}
		return (int) result;
	}
	void test(){
		std::cout << "Reversing 387: " << reverse(387) << std::endl;
		std::cout << "Reversing -145: " << reverse(-145) << std::endl;
		std::cout << "Reversing 2147483648: " << reverse(2147483648) << std::endl;
	}
}; 
