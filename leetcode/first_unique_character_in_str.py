#
# Create on 6/8/2018
#
# Author: Sylvia
#

"""
387. First Unique Character in a String

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
"""


class Solution(object):
    @staticmethod
    def first_uniq_char(s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": return -1

        mapping = {}
        ans = len(s)
        flag = -1

        for i, c in enumerate(s):
            if c in mapping:
                mapping[c] = -1
            else:
                mapping[c] = i
        for c in mapping:
            if mapping[c] != -1:
                if ans > mapping[c]:
                    flag = 1
                    ans = mapping[c]

        return ans if flag != -1 else -1


import pytest


class Test:
    @pytest.mark.parametrize('s, expect', [('love', 0), ('loveleetcode', 2),
                                           ('', -1), ('ccaa', -1)])
    def test(self, s, expect):
        assert Solution.first_uniq_char(s) is expect
