# -*- coding: utf-8 -*-
"""
824. Goat Latin

A sentence S is given, composed of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word.
For example, the word 'apple' becomes 'applema'.

If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end and so on.
Return the final sentence representing the conversion from S to Goat Latin.

Notes:

S contains only uppercase, lowercase and spaces. Exactly one space between each word.
1 <= S.length <= 150.
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        vowel_set = {"a", "e", "i", "o", "u"}
        for index, word in enumerate(S.split(), start=1):
            if word[0].lower() in vowel_set:
                one_word = word + "ma" + "a" * index
            else:
                one_word = word[1:] + word[0] + "ma" + "a" * index
            res.append(one_word)

        return " ".join(res)
