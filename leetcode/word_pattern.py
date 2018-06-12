#
# Create on 6/7/2018
#
# Author: Sylvia
#

"""
290. Word Pattern
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.
"""


class Solution(object):
    @staticmethod
    def word_pattern(pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split(' ')
        map_s, map_p = dict(), dict()
        if len(pattern) != len(str):
            return False
        else:
            for i in range(len(pattern)):
                if map_s.get(pattern[i]) is None:
                    map_s[pattern[i]] = str[i]
                if map_p.get(str[i]) is None:
                    map_p[str[i]] = pattern[i]
                if map_s[pattern[i]] != str[i] or map_p[str[i]] != pattern[i]:
                    return False
        return True


import pytest


class Test:
    @pytest.mark.parametrize('pattern, str, expect', [("abba", "dog cat cat dog", True),
                                                      ("abba", "dog cat cat fish", False),
                                                      ("aaaa", "dog cat cat dog", False),
                                                      ("abba", "dog dog dog dog", False)])
    def test(self, pattern, str, expect):
        assert Solution.word_pattern(pattern, str) is expect
