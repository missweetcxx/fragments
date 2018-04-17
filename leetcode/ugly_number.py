#
# Create on 4/17/2018
#
# Author: Sylvia
#

"""
263. Ugly Number
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not
ugly since it includes another prime factor 7.
"""


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        if num == 1:
            return True
        for p in [2, 3, 5]:
            while num % p == 0:
                num /= p
        return num == 1


import pytest


class Test:
    @pytest.mark.parametrize('num, expect', [(8, True), (14, False), (0, False), (1, True)])
    def test(self, num, expect):
        res = Solution()
        assert res.isUgly(num) is expect
