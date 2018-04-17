#
# Create on 4/17/2018
#
# Author: Sylvia
#

"""
202. Happy Number
A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops
endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^1 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = set()
        while n != 1:
            sum = 0
            if n in res:
                return False
            res.add(n)
            for d in str(n):
                sum += int(d) * int(d)
            n = sum
        return True


import pytest


class Test:
    @pytest.mark.parametrize('num, expect', [(19, True), (38, False), (1, True)])
    def test_normal(self, num, expect):
        res = Solution()
        assert res.isHappy(num) is expect
