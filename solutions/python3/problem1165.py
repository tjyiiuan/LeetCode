# -*- coding: utf-8 -*-
"""
1165. Single-Row Keyboard

There is a special keyboard with all keys in a single row.

Given a string keyboard of length 26 indicating the layout of the keyboard (indexed from 0 to 25),
initially your finger is at index 0.
To type a character, you have to move your finger to the index of the desired character.
The time taken to move your finger from index i to index j is |i - j|.

You want to type a string word. Write a function to calculate how much time it takes to type it with one finger.

Constraints:

keyboard.length == 26
keyboard contains each English lowercase letter exactly once in some order.
1 <= word.length <= 10^4
word[i] is an English lowercase letter.
"""


class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_mapping = dict((val, index) for index, val in enumerate(keyboard))
        res = 0
        last_index = 0
        for char in word:
            res += abs(last_index - key_mapping[char])
            last_index = key_mapping[char]

        return res
