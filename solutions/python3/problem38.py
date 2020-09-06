# -*- coding: utf-8 -*-
"""
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

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""


class Solution:
    def __init__(self):
        self.cache = {
            1: "1",
            2: "11",
            3: "21",
            4: "1211",
            5: "111221"
        }

    def countAndSay(self, n):
        if n in self.cache:
            return self.cache[n]

        res = self.cache[5]
        n -= 5

        while n > 0:
            res = self.say(res)
            n -= 1

        return res

    def say(self, s):
        res = ""
        count = 1
        last = s[0]
        for char in s[1:]:
            if char == last:
                count += 1
            else:
                res += str(count) + last
                last = char
                count = 1

        return res + str(count) + last
