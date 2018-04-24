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
from functools import reduce


class Solution(object):
    @staticmethod
    def add_digits_a(num):
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

    @staticmethod
    def add_digits_b(num):
        sum = int(reduce(lambda x, y: int(x) + int(y), str(num)))
        if sum < 10:
            return sum
        else:
            return Solution.add_digits_b(sum)


import pytest


class Test:
    @pytest.mark.parametrize('num, expect', [(38, 2), (0, 0), (10, 1), (9, 9)])
    def test_normal(self, num, expect):
        assert Solution.add_digits_a(num) is expect
        assert Solution.add_digits_b(num) is expect
