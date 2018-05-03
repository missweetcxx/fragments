#
# Create on 4/28/2018
#
# Author: Sylvia
#

"""
605. Can Place Flowers
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be
planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number
n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.
"""


class Solution(object):
    @staticmethod
    def can_place_flowers(flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] != 1:
                pre = 0 if i == 0 else flowerbed[i - 1]
                next = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]
                if pre == 0 and next == 0:
                    cnt += 1
                    flowerbed[i] = 1
        return cnt >= n


class Test:
    def test(self):
        assert Solution.can_place_flowers([1, 0, 0, 0, 1, 0, 0], 2) is True
        assert Solution.can_place_flowers([1, 0, 0, 0, 1], 1) is True
        assert Solution.can_place_flowers([1, 0, 0, 0, 1], 2) is False
