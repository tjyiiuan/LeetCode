#pragma once
/*
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
*/
#include <iostream>


class Solution {
public:
	int mySqrt(int x) {
		long long result = x / 2;
		long long inc = x / 4;
		long long tmp = 0;
		while (inc > 1)
		{
			tmp = result * result;
			if (tmp == x)
			{
				return result;
			}
			else
			{
				if (tmp > x)
				{
					result -= inc;
				}
				else
				{
					result += inc;
				}
				inc /= 2;
			}
		}

		if (result * result >= x)
		{
			while (result * result > x)
			{
				result -= 1;
			}
			return result;
		}

		if (result * result < x)
		{
			while (result * result <= x)
			{
				result += 1;
			}
			return result - 1;
		}
	}
	void test()	{
		int i = 2147395599;
		std::cout << i << " sqrt --> " << mySqrt(i) << std::endl;
	}
}; 
