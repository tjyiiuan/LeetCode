#pragma once
/*
67. Add Binary

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.
*/
#include <iostream>
#include <string>


class Solution {
public:
	std::string addBinary(std::string a, std::string b)	{

		int i = a.length() - 1;
		int j = b.length() - 1;
		int of = 0;
		int tmp = 0;
		std::string result = "";
		while (i >= 0 && j >= 0)
		{
			tmp = a[i] - '0' + b[j] - '0' + of;
			of = 0;
			if (tmp > 1)
			{
				of = 1;
				tmp -= 2;
			}
			result = std::to_string(tmp) + result;
			i--;
			j--;
		}
		std::cout << i << " = i, j = " << j << std::endl;

		std::string str = "";
		int ind = 0;
		if (i >= 0 || j >= 0)
		{
			if (i >= 0)
			{
				std::cout << "i" << std::endl;
				str = a;
				ind = i;
			}
			else if (j >= 0)
			{
				std::cout << "j" << std::endl;
				str = b;
				ind = j;
			}
			while (ind >= 0)
			{
				tmp = str[ind] - '0' + of;
				of = 0;
				if (tmp > 1)
				{
					of = 1;
					tmp = 0;
				}
				result = std::to_string(tmp) + result;
				ind--;
			}
		}
		if (of > 0)
		{
			result = std::to_string(of) + result;
		}

		return result;
	}
	void test()	{
		std::cout << "1 + 1 = " << addBinary("1", "1") << std::endl;
		std::cout << "1010 + 1011 = " << addBinary("1010", "1011") << std::endl;
		std::cout << "1111 + 1111 = " << addBinary("1111", "1111") << std::endl;
	}
};
