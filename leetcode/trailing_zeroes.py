#
# Create on 4/18/2018
#
# Author: Sylvia
#

"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
"""
import math

import random


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        k, res, temp = 0, 0, n
        while temp // 5 >= 1:
            k += 1
            temp = temp // 5
        for i in range(1, k + 1):
            res += n // int(math.pow(5, i))
        return res


class Test:
    @staticmethod
    def _expected_res(n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        zero_num = 0
        while res % 10 == 0:
            zero_num += 1
            res = res // 10
        return zero_num

    def test(self):
        n = random.randint(0, 1000)
        expect_res = self._expected_res(n)
        res = Solution()
        assert res.trailingZeroes(n) is expect_res
