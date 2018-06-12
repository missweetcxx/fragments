#
# Create on 6/11/2018
#
# Author: Sylvia
#

"""
409. Longest Palindrome
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be
built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.
"""

import collections


class Solution(object):
    @staticmethod
    def longest_palindrome_a(s):
        """
        :type s: str
        :rtype: int
        """
        cnt = dict(collections.Counter(s))
        odd, even = 0, 0
        odd_cnt = 0
        for k, v in cnt.items():
            if v % 2 == 0:
                even += v
            else:
                odd += v
                odd_cnt += 1
        return even + odd + 1 - odd_cnt if odd_cnt > 0 else even

    @staticmethod
    def longest_palindrome_b(s):
        flag, res = 0, 0
        for ele in set(s):
            temp = s.count(ele)
            res += temp // 2 * 2
            if not flag:
                flag = temp % 2

        return res + flag


import pytest


class Test:
    @pytest.mark.parametrize('s, expect', [('bb', 2),
                                           ('abccccdd', 7),
                                           ('asdgdd', 3)])
    def test(self, s, expect):
        assert Solution.longest_palindrome_a(s) == expect
        assert Solution.longest_palindrome_b(s) == expect
