#pragma once
/*
191. Number of 1 Bits

Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).
*/
#include <cstdint>


class Solution {
public:
	int hammingWeight(uint32_t n) {
		int res = 0;
		for (int i = 0; i < 32; i++) {
			if (n & 1 == 1) {
				res++;
			}
			n = n >> 1;
		}
		return res;
	}
};
