#pragma once
/*
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

	A -> 1
	B -> 2
	C -> 3
	...
	Z -> 26
	AA -> 27
	AB -> 28
	...
*/
#include <iostream>
#include <string>


class Solution {
public:
	int titleToNumber(std::string s) {
		long long count = 0;
		for (auto &ch : s)
		{
			count += ch - 'A' + 1;
			count *= 26;
		}
		return count / 26;
	}
	void test()	{
		std::cout << titleToNumber("A") << std::endl;
		std::cout << titleToNumber("AZ") << std::endl;
		std::cout << titleToNumber("ZY") << std::endl;
	}
};
