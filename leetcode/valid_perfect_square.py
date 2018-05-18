#
# Create on 5/18/2018
#
# Author: Sylvia
#

"""
367. Valid Perfect Square
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.
"""


class Solution(object):
    @staticmethod
    def is_perfect_square(num):
        """
        :type num: int
        :rtype: bool
        """
        l, h = 0, num
        flag = False
        while l <= h and not flag:
            mid = int((l + h) / 2)
            if mid * mid == num:
                flag = True
            elif mid * mid > num:
                h = mid - 1
            else:
                l = mid + 1
        return flag


import math
import random


class Test:
    def test(self):
        num = random.randint(0, 1000)
        assert Solution.is_perfect_square(num) == (int(math.sqrt(num)) == math.sqrt(num))
