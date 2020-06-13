#pragma once
/*
231. Power of Two

Given an integer, write a function to determine if it is a power of two.
*/
#include <iostream>


class Solution231 {
public:
	bool isPowerOfTwo(int n) {
		if (n < 1) {
			return false;
		}
		return ! (n & (n - 1));
	}
	void test() {
		std::cout << isPowerOfTwo(1) << std::endl;
		std::cout << isPowerOfTwo(1024) << std::endl;
		std::cout << isPowerOfTwo(1023) << std::endl;
	}
};
