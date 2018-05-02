#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
345. Reverse Vowels of a String
Write a function that takes a string as input and reverse only the vowels of a string.
"""


class Solution(object):
    @staticmethod
    def reverse_vowels(s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        while i<j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -= 1
            if s[i] in vowels and s[j] in vowels:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)


import pytest


class Test:
    @pytest.mark.parametrize('s, expect', [('hello', 'holle'), ('leetcode', 'leotcede'), ('','')])
    def test(self, s, expect):
        assert Solution.reverse_vowels(s) == expect
