# -*- coding: utf-8 -*-
"""
804. Unique Morse Code Words

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
"...","-","..-","...-",".--","-..-","-.--","--.."]
Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-...").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Note:

The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.
"""


class Solution:
    def uniqueMorseRepresentations(self, words):
        code_list = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                     "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
                     "...-",".--","-..-","-.--","--.."]

        res = set()
        for word in words:
            one_word = ""
            for char in word:
                one_word += code_list[ord(char) - ord('a')]
            res.add(one_word)

        return len(res)
