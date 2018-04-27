#
# Create on 4/25/2018
#
# Author: Sylvia
#

"""
231. Power of Two
Given an integer, write a function to determine if it is a power of two.
"""


class Solution(object):
    @staticmethod
    def is_power_of_two(n):
        """
        :type n: int
        :rtype: bool
        """
        power_list = []
        a = 2
        while a <= n:
            power_list.append(a)
            a = a * 2
        for i in range(2, n + 1):
            if i not in power_list:
                if n % i == 0:
                    return False
        return True

    @staticmethod
    def is_power_of_two_2(self, n):
        if n <= 0: return False
        while n > 2:
            if n % 2 != 0:
                return False
            else:
                n = n // 2
        return True


import random


class Test:
    def test_true(self):
        n = pow(2, random.randint(0, 20))
        assert Solution.is_power_of_two(n) is True

    def test_false(self):
        n = pow(2, random.randint(0, 20)) - 5
        assert Solution.is_power_of_two(n) is False
