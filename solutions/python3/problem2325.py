# -*- coding: utf-8 -*-
"""
2325. Decode the Message

You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps
to decode message are as follows:

Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.
Align the substitution table with the regular English alphabet.
Each letter in message is then substituted using the table.
Spaces ' ' are transformed to themselves.
For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we
have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').
Return the decoded message.


Constraints:

26 <= key.length <= 2000
key consists of lowercase English letters and ' '.
key contains every letter in the English alphabet ('a' to 'z') at least once.
1 <= message.length <= 2000
message consists of lowercase English letters and ' '.
"""


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key_dict = {}
        cur_index = 97
        for char in key:
            if char == " " or char in key_dict:
                continue
            key_dict[char] = chr(cur_index)
            cur_index += 1
            if cur_index == 123:
                break

        return "".join(key_dict.get(char, char) for char in message)
