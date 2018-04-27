#
# Create on 4/26/2018
#
# Author: Sylvia
#

"""
69. Sqrt(x)
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only  integer part of the result is returned.
"""


class Solution(object):
    @staticmethod
    def my_sqrt(x):
        """
        :type x: int
        :rtype: int
        """
        if x <= 1:
            return x
        l, h = 1, x - 1
        while l <= h:
            mid = int((l + h) // 2)
            sqrt = x // mid
            if sqrt == mid:
                return mid
            elif sqrt < mid:
                h = mid - 1
            else:
                l = mid + 1
        return h


import math

import random


class Test:
    def test(self):
        num = random.randint(0, 100000)
        assert Solution.my_sqrt(num) == int(math.sqrt(num))
