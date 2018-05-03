#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
680. Valid Palindrome II
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
"""


class Solution(object):
    @staticmethod
    def valid_palindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return Solution.is_palindrome(s, i, j - 1) or Solution.is_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        return True

    @staticmethod
    def is_palindrome(s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True


import pytest


class Test:
    @pytest.mark.parametrize('s, expect', [('aba', True), ('abaab', True), ('abddgbba', False)])
    def test(self, s, expect):
        assert Solution.valid_palindrome(s) == expect
