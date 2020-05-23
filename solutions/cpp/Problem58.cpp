#pragma once
/*
58. Length of Last Word

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.
*/
#include <iostream>
#include <string>


class Solution58 {
public:
	int lengthOfLastWord(std::string s)	{
		int size = s.size();
		const char space = " "[0];
		if (size == 0)
		{
			return 0;
		}
		int i = s.size() - 1;
		while (s[i] == space && i > 0)
		{
			i--;
		}
		int lastWord = i;
		while (s[i] != space && i > 0)
		{
			i--;
		}

		if (s[i] != space)
		{
			i--;
		}
		return lastWord - i;
	}
	void test()	{
		std::cout << lengthOfLastWord("Hello World") << std::endl; // 5
		std::cout << lengthOfLastWord("Hello    ") << std::endl; // 5
		std::cout << lengthOfLastWord(" He") << std::endl; // 2
		std::cout << lengthOfLastWord(" ") << std::endl; // 0
		std::cout << lengthOfLastWord("HELL") << std::endl; // 4
	}
};
