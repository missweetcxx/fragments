#
# Create on 4/17/2018
#
# Author: Sylvia
#

"""
258. Add Digits
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.
"""


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            s = 0
            for d in str(num):
                s += int(d)
            num = s
        return num


import pytest


class Test:
    @pytest.mark.parametrize('num, expect', [(38, 2), (0, 0), (10, 1), (9, 9)])
    def test_normal(self, num, expect):
        res = Solution()
        assert res.addDigits(num) is expect
