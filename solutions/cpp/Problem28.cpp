#pragma once
/*
28. Implement strStr()

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
*/
#include <iostream>
#include <string>


class Solution28 {
public:
	int strStr(std::string haystack, std::string needle) {
		if (needle == "")
		{
			return 0;
		}
		int nLength = needle.length();
		int hLength = haystack.length();
		for (int j = 0; j < hLength; j++)
		{
			if (haystack[j] == needle[0])
			{
				int tmp = j;
				if (j + nLength > hLength)
				{
					return -1;
				}

				int i = 0;
				for (; i < nLength; i++)
				{
					if (haystack[j] != needle[i])
					{
						break;
					}
					j++;
				}

				if (i == nLength)
				{
					return j - i;
				}
				j = tmp;
			}
		}

		return -1;
	}
	void test()	{
		std::cout << strStr("mississippi", "issip") << std::endl; // 4
		std::cout << strStr("a", "a") << std::endl; // 0
		std::cout << strStr("hello", "lla") << std::endl; // -1
	}
};
