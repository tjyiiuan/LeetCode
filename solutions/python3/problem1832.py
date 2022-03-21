# -*- coding: utf-8 -*-
"""
1832. Check if the Sentence Is Pangram

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false
otherwise.


Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        all_char = set(chr(i) for i in range(97, 123))
        for char in sentence:
            if char in all_char:
                all_char.remove(char)

        return len(all_char) == 0
