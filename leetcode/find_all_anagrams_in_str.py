#
# Create on 5/14/2018
#
# Author: Sylvia
#

"""
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100

The order of output does not matter.
"""
from collections import Counter


class Solution(object):
    @staticmethod
    def find_anagrams(s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        p_map = Counter(p)
        s_map = Counter(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            s_map[s[i]] += 1
            if s_map == p_map:
                res.append(i - len(p) + 1)
            s_map[s[i - len(p) + 1]] -= 1
            if s_map[s[i - len(p) + 1]] == 0:
                del s_map[s[i - len(p) + 1]]
        return res


import pytest


class Test:
    @pytest.mark.parametrize('s, p, res', [('cbaebabacd', 'abc', [0, 6]),
                                           ('abab', 'ab', [0, 1, 2])])
    def test(self, s, p, res):
        assert Solution.find_anagrams(s, p) == res
