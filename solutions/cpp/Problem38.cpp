#pragma once
/*
38. Count and Say
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.
 */
#include <iostream>
#include <string>


class Solution {
public:
	std::string readStr(std::string &str) {
		int size = str.length();
		if (size == 1)
		{
			return "1" + str;
		}
		else
		{
			std::string result = "";
			char last = str[0];
			int count = 1;
			for (int i = 1; i < size; i++)
			{
				if (str[i] == last)
				{
					count += 1;
				}
				else
				{
					result += std::to_string(count) + last;
					last = str[i];
					count = 1;
				}
			}
			return result + std::to_string(count) + last;
		}
	}
	std::string countAndSay(int n)	{
		std::string result = "1";
		for (int i = 1; i < n; i++)
		{
			result = readStr(result);
		}
		return result;
	}
	void test() {
	std::cout << countAndSay(1) << std::endl;
	std::cout << countAndSay(4) << std::endl;
	std::cout << countAndSay(10) << std::endl;
	}
};
