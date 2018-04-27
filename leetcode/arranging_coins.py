#
# Create on 4/26/2018
#
# Author: Sylvia
#

"""
441. Arranging Coins
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.
"""


class Solution(object):
    @staticmethod
    def arrange_coins_a(n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l <= h:
            mid = int((l + h) // 2)
            sum = (1 + mid) * mid // 2
            if sum == n:
                return mid
            elif sum < n:
                l = mid + 1
            else:
                h = mid - 1
        return h

    @staticmethod
    def arrange_coins_b(n):
        level = 1
        while n > 0:
            n -= level
            level += 1
        return level - 1 if n == 0 else level - 2


import random


class Test:
    def test(self):
        num = random.randint(0, 100000)
        assert Solution.arrange_coins_a(num) == Solution.arrange_coins_b(num)
