#
# Create on 5/2/2018
#
# Author: Sylvia
#

"""
633. Sum of Square Numbers
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.
"""
import math


class Solution(object):
    @staticmethod
    def judge_square_sum(c):
        """
        :type c: int
        :rtype: bool
        """
        sqr = int(math.sqrt(c))
        i, j = 0, sqr
        while i <= j:
            if i * i + j * j == c:
                return True
            elif i * i + j * j < c:
                i += 1
            else:
                j -= 1
        return False


import pytest


class Test:
    @pytest.mark.parametrize('input, expect', [(3, False), (5, True), (0, True)])
    def test(self, input, expect):
        assert Solution.judge_square_sum(input) is expect
