#pragma once
/*
13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together.
Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
Instead, the number four is written as IV. Because the one is before the five we subtract it making four.
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
	I can be placed before V (5) and X (10) to make 4 and 9.
	X can be placed before L (50) and C (100) to make 40 and 90.
	C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
*/
#include <iostream>
#include <string>
#include <map>


class Solution13 {
public:
	Solution13() {
		int pre = 1;
		for (auto &ch : "IXC")
		{
			rPre[ch] = pre;
			pre *= 10;
		}

		rRes["V"[0]] = 5;
		rRes["L"[0]] = 50;
		rRes["D"[0]] = 500;
		rRes["M"[0]] = 1000;
	}

	int romanToInt(std::string s) {
		std::string refer = "IXCVLDM";
		int size = s.length();
		int result = 0;
		for (int i = 0; i < size; i++)
		{
			char ch = s[i];
			if (rRes.find(ch) != rRes.end())
			{
				result += rRes[ch];
			}
			else if (i != size - 1)
			{
				if (ch == refer[0])
				{
					if (s[i + 1] == refer[3] || s[i + 1] == refer[1])
					{
						result -= rPre[ch];
					}
					else
					{
						result += rPre[ch];
					}
				}
				else if (ch == refer[1])
				{
					if (s[i + 1] == refer[4] || s[i + 1] == refer[2])
					{
						result -= rPre[ch];
					}
					else
					{
						result += rPre[ch];
					}
				}
				else if (ch == refer[2])
				{
					if (s[i + 1] == refer[5] || s[i + 1] == refer[6])
					{
						result -= rPre[ch];
					}
					else
					{
						result += rPre[ch];
					}
				}
				else
				{
					result += rPre[ch];
				}
			}
			else
			{
				result += rPre[ch];
			}
		}
		return result;
	}
	void test()	{
		std::cout << romanToInt("III") << std::endl; // 3
		std::cout << romanToInt("IX") << std::endl; // 9
		std::cout << romanToInt("LVIII") << std::endl; // 58
		std::cout << romanToInt("MCMXCIV") << std::endl; // 1994
	}
private:
	std::map<char, int> rPre;
	std::map<char, int> rRes;
	std::string refer = "IXCVLDM";
}; 
