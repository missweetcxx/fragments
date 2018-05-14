#
# Create on 5/14/2018
#
# Author: Sylvia
#

"""
242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.
"""


class Solution(object):
    @staticmethod
    def is_anagram(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_map, t_map = {}, {}
        for char in s:
            if s_map.get(char) is None:
                s_map[char] = 0
            s_map[char] += 1
        for char in t:
            if t_map.get(char) is None:
                t_map[char] = 0
            t_map[char] += 1
        return s_map == t_map


class Test:
    def test_true(self):
        s = "anagram"
        t = "nagaram"
        assert Solution.is_anagram(s, t) is True

    def test_false(self):
        s = "rat"
        t = "car"
        assert Solution.is_anagram(s, t) is False
