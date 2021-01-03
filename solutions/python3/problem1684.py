# -*- coding: utf-8 -*-
"""
1684. Count the Number of Consistent Strings

You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.

Return the number of consistent strings in the array words.

Constraints:

1 <= words.length <= 104
1 <= allowed.length <= 26
1 <= words[i].length <= 10
The characters in allowed are distinct.
words[i] and allowed contain only lowercase English letters.
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words) -> int:
        allowed_char = set(allowed)
        count = 0
        for word in words:
            if set(word).issubset(allowed_char):
                count += 1

        return count
