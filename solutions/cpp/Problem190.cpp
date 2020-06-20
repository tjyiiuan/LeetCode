#pragma once
/*
190. Reverse Bits

Reverse bits of a given 32 bits unsigned integer.
*/
#include <cstdint>


class Solution {
public:
	uint32_t reverseBits(uint32_t n) {
		uint32_t res = 0;
		for (int i = 0; i < 32; i++) {
			res = res << 1;
			if (n & 1 == 1) {
				res += 1;
			}
			n = n >> 1;
		}
		return res;
	}
};
