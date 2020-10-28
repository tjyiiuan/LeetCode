# -*- coding: utf-8 -*-
"""
1108. Defanging an IP Address

Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Constraints:

The given address is a valid IPv4 address.
"""


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
