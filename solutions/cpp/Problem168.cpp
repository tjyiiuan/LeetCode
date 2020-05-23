#pragma once
/*
168. Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

	1 -> A
	2 -> B
	3 -> C
	...
	26 -> Z
	27 -> AA
	28 -> AB
	...
*/
#include <iostream>
#include <string>


class Solution168 {
public:
	std::string convertToTitle(int n) {
		std::string result = "";
		while (n > 0)
		{
			int cur = n % 26 - 1;
			n /= 26;
			if (cur == -1)
			{
				cur += 26;
				n -= 1;
			}
			result = (char)('A' + cur) + result;
		}
		return result;
	}
	void test()	{
		std::cout << convertToTitle(28) << std::endl;
		std::cout << convertToTitle(52) << std::endl;
		std::cout << convertToTitle(701) << std::endl;
	}
}; 
