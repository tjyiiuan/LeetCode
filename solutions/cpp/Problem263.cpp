#pragma once
/*
263. Ugly Number

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Note:
1 is typically treated as an ugly number.
Input is within the 32-bit signed integer range: [−2^31,  2^31 − 1].
*/
#include <iostream>


class Solution {
public:
	bool isUgly(int num) {
		if (num <= 0) {
			return false;
		}
		num = fullDivide(num, 2);
		num = fullDivide(num, 3);
		num = fullDivide(num, 5);
		return num == 1;
	}
	int fullDivide(int num, int fac) {
		int res;
		while (num >= 1) {
			res = num % fac;
			if (res == 0) {
				num /= fac;
			}
			else {
				break;
			}
		}
		return num;
	}
	void test() {
		std::cout << isUgly(6) << std::endl;
		std::cout << isUgly(8) << std::endl;
		std::cout << isUgly(14) << std::endl;
	}
};
