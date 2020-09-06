# -*- coding: utf-8 -*-
"""
93. Restore IP Addresses

Given a string s containing only digits, return all possible valid IP addresses that can be obtained from s.
You can return them in any order.

A valid IP address consists of exactly four integers, each integer is between 0 and 255,
separated by single dots and cannot have leading zeros.
For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses and "0.011.255.245",
"192.168.1.312" and "192.168@1.1" are invalid IP addresses.
"""


class Solution:
    def restoreIpAddresses(self, s):
        return [".".join(i) for i in self.seperate(s, 4)]

    def seperate(self, s, n):
        if not s or n == 0 or n > len(s) or len(s) > 3 * n:
            return []
        elif n == 1:
            if int(s) > 255:
                return []
            elif s[0] == "0" and len(s) > 1:
                return []
            else:
                return [[s]]
        elif n == len(s):
            return [[c for c in s]]
        else:
            res = []
            for i in range(1, 4):
                f = int(s[:i])
                if f > 255:
                    continue
                elif s[0] == "0" and i > 1:
                    continue

                for r in self.seperate(s[i:], n - 1):
                    res.append([s[:i]] + r)

            return res
